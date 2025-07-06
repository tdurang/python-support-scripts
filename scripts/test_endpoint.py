import requests
import time

def test_endpoint(url, method='GET', data=None):
    try:
        print(f"\n🔍 Testing {method} request to: {url}")
        start_time = time.time()

        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        else:
            print("❌ Only GET and POST methods are supported.")
            return

        duration = round((time.time() - start_time) * 1000, 2)  # ms

        print(f"✅ Status Code: {response.status_code}")
        print(f"⏱ Response Time: {duration} ms")
        print(f"📦 Response Body (truncated):\n{response.text[:200]}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error during request: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    test_endpoint("https://github.com/tdurang/python-support-scripts/tree/main#")