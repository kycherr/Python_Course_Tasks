# def check_files_size_equality(directory):
#     import os
#     try:
#         files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
#         if not files:
#             print("No files found in the directory.")
#             return False
#         first_file_size = os.path.getsize(os.path.join(directory, files[0]))
#         for file in files[1:]:
#             file_path = os.path.join(directory, file)
#             file_size = os.path.getsize(file_path)

#         if file_size != first_file_size:
#             print(f"Files in the directory do not have the same size.")
# 
#             return False
        #     print("All files in the directory have the same size.")
        #     return True
        # except Exception as e:
        #     print(f"Error: {e}")
        #     return False

# check_files_size_equality('src')
