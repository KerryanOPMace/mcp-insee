import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.insee.fr/api-sirene/3.11"

def test_siren():
    url = f"{BASE_URL}/siret/44302124100072"
    headers = {
        "Content-Type": "application/json",
        "X-INSEE-Api-Key-Integration": f"{API_KEY}"
    }
    response=requests.get(url, headers=headers)
    data=response.json()
    print(data["etablissement"]["adresseEtablissement"])

test_siren()