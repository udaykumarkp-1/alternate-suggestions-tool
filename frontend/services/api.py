import requests

BASE_URL = "https://alternate-backend.onrender.com"

TIMEOUT = 30


# ---------------- SAVE DATA ----------------

def save_payload(payload):
    """
    Save processed mapping results to the backend database.
    """

    try:
        response = requests.post(
            f"{BASE_URL}/save",
            json=payload,
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            return True

        return False

    except Exception as e:
        print("SAVE ERROR:", e)
        return False


# ---------------- SEARCH ----------------

def search_api(query):
    """
    Search products or molecules in the stored database.
    """

    if not query:
        return []

    try:
        response = requests.get(
            f"{BASE_URL}/search",
            params={"q": query},
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            return response.json()

        return []

    except Exception as e:
        print("SEARCH ERROR:", e)
        return []


# ---------------- CHECK DATABASE STATUS ----------------

def check_data_status():
    """
    Check if database contains any stored mappings.
    """

    try:
        response = requests.get(
            f"{BASE_URL}/has_data",
            timeout=TIMEOUT
        )

        if response.status_code == 200:
            return response.json()

        return {"has_data": False}

    except Exception as e:
        print("STATUS ERROR:", e)
        return {"has_data": False}