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

