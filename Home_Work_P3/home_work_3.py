# Розробіть скрипт, який відкриває існуючий текстовий файл, 
# зчитує його вміст та виводить його на екран.
import os
source_file = input("Enter file name: ")
if os.path.isfile(source_file):
    with open(source_file, 'r') as file:
        content = file.read()
        print(content)
else:
    print("File not exist!")