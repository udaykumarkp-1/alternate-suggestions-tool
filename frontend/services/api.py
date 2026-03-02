import requests

API_URL = "https://alternate-backend.onrender.com"


# ---------------- CHECK IF DATA EXISTS ----------------
def check_has_data():
    try:
        res = requests.get(f"{API_URL}/has_data", timeout=10)

        if res.status_code == 200:
            return res.json().get("has_data", False)

        return False

    except requests.exceptions.RequestException:
        return False


# ---------------- SAVE PROCESSED PAYLOAD ----------------
def save_payload(payload):
    try:
        res = requests.post(
            f"{API_URL}/save",
            json=payload,
            timeout=60
        )

        return res

    except requests.exceptions.RequestException as e:
        raise Exception("Backend save failed. Please try again.")


# ---------------- SEARCH PRODUCTS ----------------
def search_products(query):
    try:
        res = requests.get(
            f"{API_URL}/search",
            params={"q": query},
            timeout=30
        )

        return res

    except requests.exceptions.RequestException:
        raise Exception("Search request failed. Backend not reachable.")