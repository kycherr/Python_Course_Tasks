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