def parse_log_file(filepath, keyword):
    with open(filepath, 'r') as file: 
        for line in file: 
            if keyword.lower() in line.lower():
                print(line.strip())

# For testing
if __name__ == "__main__":
    parse_log_file('app.log', 'error')