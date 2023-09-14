import os


def list_all_subdirectories(folder_path):
    subdirectories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    if subdirectories:
        print(f"Subdirectories in '{folder_path}':")
        for subdir in subdirectories:
            subdir_path = os.path.join(folder_path, subdir)
            print(subdir_path)
            list_all_subdirectories(subdir_path)  # Recursively list subdirectories


if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    if os.path.isdir(folder_path):
        list_all_subdirectories(folder_path)
    else:
        print("Invalid folder path.")
