import requests
import logging

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_URL = "https://fakestoreapi.com/users"

def fetch_users():
    logging.info("Starting API call to fetch users")

    try:
        response = requests.get(API_URL, timeout=10)

        logging.info(f"API response status code: {response.status_code}")

        response.raise_for_status()  # raises exception for 4xx/5xx

        data = response.json()

        logging.info(f"Number of records received: {len(data)}")

        return data

    except requests.exceptions.Timeout:
        logging.error("API request timed out")
        return []

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return []

if __name__ == "__main__":
    users = fetch_users()
    logging.info("API fetch completed")
