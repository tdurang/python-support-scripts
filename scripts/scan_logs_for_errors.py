import os

def scan_logs_for_keyword(folder_path, keyword):
    keyword = keyword.lower()
    found = False

    for filename in os.listdir(folder_path):
        if filename.endswith(".log"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        if keyword in line.lower():
                            print(f"[{filename}] Line {i}: {line.strip()}")
                            found = True
            except Exception as e:
                print(f"❌ Error reading {filename}: {e}")

    if not found:
        print(f"✅ No occurrences of '{keyword}' found in .log files.")

# Uso de prueba
if __name__ == "__main__":
    scan_logs_for_keyword("example_logs", "error")