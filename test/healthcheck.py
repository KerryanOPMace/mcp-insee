import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.insee.fr/api-sirene/3.11"  

def test_healthcheck():
    url = f"{BASE_URL}/informations"
    headers = {
        "Content-Type": "application/json",
        "X-INSEE-Api-Key-Integration": f"{API_KEY}"
    }
    response = requests.get(url, headers=headers)
    print(response.json())

test_healthcheck()