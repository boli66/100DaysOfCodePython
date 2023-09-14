import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except Exception as e:
        print(f"Error counting lines in '{file_path}': {e}")
        return 0

def count_lines_in_directory(directory_path):
    total_lines = 0
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            lines = count_lines_in_file(file_path)
            total_lines += lines
            print(f"File: {file_path} - Lines: {lines}")


    return total_lines
print(os.path.abspath("../../"))
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    total_lines = count_lines_in_directory(folder_path)
    print(f"Total lines in all files: {total_lines}")
