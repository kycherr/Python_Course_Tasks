import json
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from math import sin, cos, tan

app = Flask(__name__)
app.secret_key = 'wawawawa2024'

def get_users():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def load_operations():
    try:
        with open('operations.json', 'r') as file:
            operations = json.load(file)
    except FileNotFoundError:
        operations = []
    return operations

def save_operations(operations):
    with open('operations.json', 'w') as file:
        json.dump(operations, file, indent=4)

def save_operation(user_id, operation, num1, num2, result):
    operations = load_operations()
    operation_id = len(operations) + 1
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    operation_data = {
        "id": operation_id,
        "date": date,
        "operation": f"{num1} {operation} {num2} = {result}",
        "user_id": user_id
    }

    operations.append(operation_data)
    save_operations(operations)

def is_user_registered(user_id):
    users = get_users()
    user = next((user for user in users if user['user_id'] == user_id), None)
    return user is not None and user.get('registered', False)

@app.route('/')
def index():
    return render_template('index.html', registered=is_user_registered(session.get('user_id', None)))

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        if 'user_id' in session:
            num1 = float(request.form['num1'])
            operation = request.form['operation']

            if operation not in ('+', '-', '*', '/', 'sin', 'cos', 'tan', 'cot'):
                raise ValueError("Invalid operation")

            result = 0

            if operation in ('+', '-', '*', '/'):
                num2 = float(request.form['num2'])

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        raise ZeroDivisionError("Cannot divide by zero")

                save_operation(session['user_id'], operation, num1, num2, result)
            else:
                if operation == 'sin':
                    result = sin(num1)
                elif operation == 'cos':
                    result = cos(num1)
                elif operation == 'tan':
                    result = tan(num1)
                elif operation == 'cot':
                    result = 1 / tan(num1)

                save_operation(session['user_id'], operation, num1, None, result)

        else: 
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation not in ('+', '-', '*','/'):
                raise ValueError("Invalid operation")

            result = 0

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ZeroDivisionError("Cannot divide by zero")

        return render_template('index.html', result=result, registered=is_user_registered(session.get('user_id', None)))

    except ValueError as ve:
        return render_template('index.html', error=f"Error: {ve}", registered=is_user_registered(session.get('user_id', None)))
    except ZeroDivisionError as zde:
        return render_template('index.html', error=f"Error: {zde}", registered=is_user_registered(session.get('user_id', None)))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = get_users()
        user_id = len(users) + 1

        new_user = {"user_id": user_id, "username": username, "password": password, "registered": True}
        users.append(new_user)

        save_users(users)

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = get_users()
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)

        if user:
            session['user_id'] = user['user_id']
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/history')
def history():
    if 'user_id' in session:
        user_id = session['user_id']
        user_operations = [op for op in load_operations() if op['user_id'] == user_id]
        return render_template('history.html', operations=user_operations)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
