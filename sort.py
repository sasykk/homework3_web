import os
from shutil import move
from concurrent.futures import ThreadPoolExecutor


def process_folder(path):
    extensions = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext.lower()  
            extensions.setdefault(ext, []).append(os.path.join(root, file))   

    for ext, files in extensions.items():
        folder_name = ext[1:] if ext.startswith('.') else ext
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file_path in files:
            move(file_path, folder_path)

def main():
    folder_path = 'C:/Users/User/python/GOIT/homeworks/web/homework3_web_test'  
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(process_folder, folder_path)

if __name__ == "__main__":
    main()
