# Розробіть скрипт, який відкриває існуючий текстовий файл, 
# зчитує його вміст та виводить його на екран.

# import os
# source_file = input("Enter file name: ")
# if os.path.isfile(source_file):
#     with open(source_file, 'r') as file:
#         content = file.read()
#         print(content)
# else:
#     print("File not exist!")

# Створіть програму, яка переіменовує файл з одного імені в інше. 
# rename_file(path_to_file, new_name)

# import os
# source_file = input("Enter file to rename: ")
# destination_file = input("Enter final name of file: ")
# if os.path.isfile(source_file):
#     os.rename(source_file, destination_file)
# else:
#     print("File not exist!")

# Напишіть скрипт для копіювання вмісту одного текстового файлу в інший.
# copy_to_file(source_file, new_file)

# import os
# source_file = input("Enter src file: ")
# destination_file = input("Enter dst file: ")
# if os.path.isfile(source_file):
#     with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
#         for line in src:
#             dst.write(line)
# else:
#     print('Source file does not exists')

# Розробіть програму, яка визначає кількість слів у текстовому файлі.
# count_words(path_to_file)

# def count_words(file):
#     import os
#     words_num = 0
#     if os.path.isfile(file):
#         with open(file, 'r') as f:
#             content = f.read()
#             lines = content.split()
#             words_num += len(lines)
#         print(f"Number of words is: {words_num}")
#     else:
#         print('Source file does not exists')

# file_name = input("Enter file to count: ")
# count_words(file_name)

# Створіть скрипт, який видаляє текстовий файл. 
# remove_file(path_file). Повертає помилку якщо файла не існує

# def del_file(file):
#     import os
#     if os.path.isfile(file):
#         os.remove(file)
#         print(f"File {file} Was removed!")
#     else:
#         print(f'File {file} does not exists')

# del_file('test')

# Напишіть програму, яка додає новий рядок до існуючого текстового файлу.
# add_data_to_file(path_file , text).

# def add_data_to_file(path_file , text):
#     import os
#     if os.path.isfile(path_file):
#         with open(path_file, "a+") as file:
#             file.write("\n"+text)
#     else:
#         print(f"The file '{path_file}' doesn't exist.")

# add_data_to_file('random.txt', 'Data from function')

# Розробіть скрипт, який перевіряє наявність файлу за заданим ім'ям 
# та повідомляє користувача про результат. функція має повертати True/False

# def find_file(name):
#     import os
#     filepath = os.path.join(os.getcwd(),name)
#     if os.path.isfile(filepath):
#         return True
#     return False
            
# print(find_file('random.txt'))

# Створіть програму, яка шукає вказаний текст у файлі 
# та виводить номери рядків, де цей текст знаходиться
# find_text(path_file, search_text )

# def find_text(path_file, search_text):
#     lines = []
#     with open(path_file, 'r') as f:
#         for num, line in enumerate(f, start=1):
#             if search_text in line:
#                 lines.append(num)
#                 if lines:
#                     print(f'Text found at lines: {lines}')
#                 else:
#                     print(f'Text not found at any lines')
# find_text('random.txt', 'ipsum')

# Напишіть скрипт, який сортує вміст текстового файлу за алфавітом і 
# зберігає відсортований результат у новому файлі. sort_data_in_file(file_path). 
# Резульаттом має бути новий файл з наступною назвою {file_path}_sorted

#def sort_data_in_file(file_path):
#    import os
#    source_file = input("Enter src file: ")
#    if os.path.isfile(source_file):
#        with open(source_file, 'r') as src, open(source_file + '_sorted', 'w') as dst:
#            dst.write('\n'.join(sorted(src.read().splitlines())))
#    else:
#        print('Source file not exists')
#sort_data_in_file('random.txt')
#####
### Part 2 ####
#####
#Розробіть функцію, яка перевіряє розмір файлу і повідомляє користувача, 
#чи він перевищує заданий ліміт. is_greater_size(file_path, limit)

#def is_greater_size(file_path, limit):
 #   import os
 #   if os.path.isfile(file_path):
 #       size = os.path.getsize(file_path) / (1024)
 #       if size > limit:
 #           print(f"File size is {size} bytes")
 #       else:
 #           print('File not exists')
#
#print(is_greater_size('random.txt', 0.200))

# Напишіть скрипт для копіювання усіх файлів з одного каталогу в інший. 
# copy_folder(from_folder , to_folder)

# def copy_folder(from_folder, to_folder):
#     import os
#     import shutil
#     if not os.path.exists(from_folder):
#         print(f"Error '{from_folder}' not exist")
#         return
#     if not os.path.exists(to_folder):
#         print(f"Create folder '{to_folder}'.")
#         os.makedirs(to_folder)
#     files = os.listdir(from_folder)
#     for file_name in files:
#         source_path = os.path.join(from_folder, file_name)
#         destination_path = os.path.join(to_folder, file_name)
#         shutil.copy2(source_path, destination_path)
#         print(f"Copy: {file_name}")
#     print(f"All fiels will copy from '{from_folder}' to '{to_folder}'.")
# copy_folder("src", "dest")

# Створіть функцію, яка читає CSV-файл і виводить на екран лише певні стовпці.

# def read_csv_columns(csv_file_path, columns):
#     import csv
#     try:
#         with open(csv_file_path, 'r', newline='') as csv_file:
#             reader = csv.DictReader(csv_file, delimiter=';')
#             for col in columns:
#                 if col not in reader.fieldnames:
#                     print(f"Error! Column {col} does not exist in the file.")
#                     return
#             print("\t".join(columns))
#             for row in reader:
#                 row_data = [row[col] for col in columns]
#                 print('\t'.join(row_data))
#     except FileNotFoundError:
#         print(f"Error: File {csv_file_path} does not exist.")
#     except Exception as e:
#         print(f"Error: {e}")
# read_csv_columns('src/test.csv', ['Username'])

# Напишіть скрипт, який створює архів з кількох файлів та розпаковує його. має бути дві функції
#     - create_archive (*files)
#     - unpacking_archive(path_to_archive)

# def create_archive(*files, archive_name, archive_type):
#     import shutil
#     try:
#         shutil.make_archive(archive_name, archive_type, *files)
#         print(f"Archive {archive_name}.{archive_type} is created successfully")
#     except Exception as e:
#         print(f"Error is {e}")

# def  unpacking_archive(archive_path):
#     import shutil
#     try:
#         shutil.unpack_archive(archive_path, extract_dir='unpacked_files')
#         print(f"Archive war unpacked in 'unpacked_files' dir")
#     except Exception as e:
#         print(f"Error while unpacking: {e}")
# files = ['src', 'test.csv']
# create_archive(*files, archive_name='my_archive', archive_type='zip')
# unpacking_archive('my_archive.zip')

#  Розробіть функцію, яка змінює права доступу до файлу 
#  (наприклад, робить його доступним лише для читання або запису).

# def chmod_file(file_path, mode):
#     import os
#     try:
#         os.chmod(file_path, mode)
#         print(f"Chmod for {file_path} now is {mode}")
#     except Exception as e:
#         print(f"Error is {e}")

# chmod_file('random.txt', 400)

# Створіть функцію, яка виводить список всіх файлів у заданому каталозі та його підкаталогах.

# def ls_dir(dir):
#     import os
#     try:
#         for root, dirs, files in os.walk(dir):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 print(file_path)
#     except Exception as e:
#         print(f"Error {e}")
# ls_dir('src')

# Напишіть функцію, яка масово перейменовує файли у заданому каталозі за певним шаблоном. 
# Додайте до кожної назви файла префікс "rename_"

# def rename_files(dir):
#     import os
#     try:
#         files = os.listdir(dir)
#         for file in files:
#             old_path = os.path.join(dir, file)
#             new_name = f"rename_{file}"
#             new_path = os.path.join(dir, new_name)
#             counter = 1
#             while os.path.exists(new_path):
#                 new_name = f"rename_{counter}_{file}"
#                 new_path = os.path.join(dir, new_name)
#                 counter += 1
#             os.rename(old_path, new_path)
#             print(f"Raname: {file} -> {new_name}")
#     except Exception as e:
#         print(f"Error {e}")
        
# rename_files('src')

# Створіть скрипт, який зчитує XML-файл та витягує з нього певну інформацію.

# def read_xml(file):
#     import xml.etree.ElementTree as ET
#     try:
#         tree = ET.parse(file)
#         root = tree.getroot()
#         for book in root.findall('.//book'):
#             title = book.find('title').text
#             author = book.find('author').text
            
#             print(f"Title: {title}, Author: {author}")
#     except Exception as e:
#         print(f"Error {e}")
        
# read_xml('src/test.xml')

# Розробіть скрипт, який переформатовує CSV-файл, 
# видаляючи дублікати рядків та зберігаючи результат у новому файлі.

# def rem_dup(src_f, dst_f):
#     import csv
#     try:
#         with open(src_f, 'r', newline='') as infile, open(dst_f, 'w', newline='') as outfile:
#             reader = csv.reader(infile)
#             writer = csv.writer(outfile)
#             seen_rows = set()
#             for row in reader:
#                 tupple_row = tuple(row)
#                 if tupple_row not in seen_rows:
#                     seen_rows.add(tupple_row)
#                     writer.writerow(row)
#                     print(f"Added unic row: {row}")
#             print("Dupliocates is found! Results saved in new file")
#     except Exception as e:
#         print(f"Error is {e}")
        
# rem_dup('src/rename_test.csv', 'without_dup.csv')

# Створіть функцію для пошуку файлів з певним розширенням 
# у вказаному каталозі та всіх його підкаталогах..

# def find_files_ext(dir, ext):
#     import os
#     found_files = []
#     try:
#         for root, dirs, files in os.walk(dir):
#             for file in files:
#                 if file.endswith(ext):
#                     file_path = os.path.join(root, file)
#                     found_files.append(file_path)
#     except Exception as e:
#         print(f"Error {e}")
#     print(found_files)

# find_files_ext('src', '.xml')

# Створіть функцію для створення текстового файлу, 
# в якому кожний рядок містить назву файлу,
# його розмір та дату створення, для всіх файлів у вказаному каталозі.

# def info_file(directory, output_file):
#     import os
#     from datetime import datetime
#     try:
#         with open(output_file, 'w') as out:
#             for root, dirs, files in os.walk(directory):
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     file_size = os.path.getsize(file_path)
#                     create_time = os.path.getctime(file_path)
#                     create_time_str = datetime.fromtimestamp(create_time).strftime('%Y-%m-%d %H:%M:%S')
#                     out.write(f"File: {file}\nSize: {file_size} bytes\nCreate time: {create_time_str}\n\n")
#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# info_file('src', 'info.txt')           