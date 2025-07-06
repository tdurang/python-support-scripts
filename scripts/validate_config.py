import json

def validate_json_config(file_path, required_keys):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            print(f"✅ {file_path} is a valid JSON file.")

            missing = [key for key in required_keys if key not in config]
            if missing:
                print(f"⚠️ Missing required keys: {missing}")
            else:
                print("✅ All required keys are present.")

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format in {file_path}: {e}")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Uso de prueba
if __name__ == "__main__":
    required = ["apiKey", "projectId", "databaseURL"]
    validate_json_config("firebase_config_test.json", required)