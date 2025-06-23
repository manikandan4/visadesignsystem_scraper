import os
import requests

# Define output directory
TEST_OUTPUT_DIR = "input"
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

def fetch_json():
    """
    Fetch JSON content directly from the API endpoint using requests.
    """
    url = "https://design.visa.com/api/nova-react-2.5.4.json"

    try:
        # Disable SSL verification temporarily
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        json_content = response.json()
        save_to_file(json_content)
        print("⚠️ Warning: SSL verification is disabled. This is not secure and should only be used for testing.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch JSON: {e}")

def save_to_file(content):
    """
    Save the JSON content to a file.
    """
    filename = os.path.join(TEST_OUTPUT_DIR, "nova-react-2.5.4.json")

    with open(filename, "w", encoding="utf-8") as f:
        import json
        json.dump(content, f, indent=4)

    print(f"✅ JSON content saved to {filename}")

# Replace aiohttp with requests for synchronous fetching
if __name__ == "__main__":
    fetch_json()
