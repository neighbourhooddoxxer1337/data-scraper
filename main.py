import requests

EMAIL = "awang.dani1609@gmail.com"
PASSWORD = "iaminvincible!!!!!!"

LOGIN_URL = "https://data.bn-marketplace.net/login"
SCRAPE_URL = "https://data.bn-marketplace.net/api/vendor-data"

session = requests.Session()

def login():
    payload = {
        "email": EMAIL,
        "password": PASSWORD
    }
    response = session.post(LOGIN_URL, data=payload)
    if response.status_code == 200 and "auth_token" in response.json():
        print("[+] Login successful.")
        return True
    else:
        print("[-] Login failed.")
        return False

def scrape_data():
    print("[*] Scraping vendor data...")
    response = session.get(SCRAPE_URL)
    if response.status_code == 200:
        data = response.json()
        for vendor in data.get("vendors", []):
            print(f"{vendor['name']} - {vendor['category']} - {vendor['rating']} stars")
    else:
        print("[-] Failed to retrieve data.")

if __name__ == "__main__":
    if login():
        scrape_data()
