import os
from datetime import datetime

def list_recent_files(folder_path, limit=10):
    try:
        files = [
            (file, os.path.getmtime(os.path.join(folder_path, file)))
            for file in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, file))
        ]
        sorted_files = sorted(files, key=lambda x: x[1], reverse=True)

        print(f"\nTop {limit} recently modified files in '{folder_path}':\n")
        for file, mod_time in sorted_files[:limit]:
            readable_time = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{file} - Last modified: {readable_time}")

    except Exception as e:
        print(f"Error: {e}")

# Uso de prueba
if __name__ == "__main__":
    list_recent_files('.', limit=5)
