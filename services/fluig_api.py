import requests
from config import FLUIG_BASE_URL, FLUIG_DATASET_ID, FLUIG_USER, FLUIG_PASS

def get_chamados():
    url = f"{FLUIG_BASE_URL}/dataset/search"

    params = {
        "datasetId": FLUIG_DATASET_ID,
        "limit": 25
    }

    r = requests.get(url, params=params, auth=(FLUIG_USER, FLUIG_PASS))

    data = r.json()

    return data.get("content", [])