import requests
from getpass import getpass

url = "https://captcha-app-4sqx.onrender.com/captcha"

token = getpass("Enter your Access Token: ").strip()

headers = {
    "Authorization": token
}

response = requests.get(url, headers=headers, timeout=30)

print("Status Code:", response.status_code)
print("Response:", response.text)