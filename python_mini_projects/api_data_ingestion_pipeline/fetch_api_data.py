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

        response.raise_for_status()

        data = response.json()
        logging.info(f"Number of records received: {len(data)}")

        return data

    except requests.exceptions.Timeout:
        logging.error("API request timed out")
        return []

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return []


def flatten_users(users):
    """
    Flattens user records based on expected API schema.
    Strict approach: does not guess or adapt broken schemas.
    """

    flattened = []

    for user in users:
        record = {
            "user_id": user.get("id"),
            "email": user.get("email"),
            "username": user.get("username"),
            "phone": user.get("phone"),
            "first_name": user.get("name", {}).get("firstname"),
            "last_name": user.get("name", {}).get("lastname"),
            "city": user.get("address", {}).get("city"),
            "zipcode": user.get("address", {}).get("zipcode"),
        }

        flattened.append(record)

    return flattened


if __name__ == "__main__":
    users = fetch_users()
    logging.info("API fetch completed")

    flattened_users = flatten_users(users)

    logging.info(f"Flattened records count: {len(flattened_users)}")

    if flattened_users:
        logging.info(f"Sample flattened record: {flattened_users[0]}")
