import requests
import logging 
from requests.exceptions import Timeout, RequestException



def fetch_api_data():

    url = 'https://jsonplaceholder.typicode.com/users'

    try:
        logging.info("Starting API request")
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        
        logging.info(f" Fetched api response with the status code :{response.status_code}")

        return response.json()

    except Timeout as e:
        logging.error(f"Api failed timeout {e}")
        raise
    except RequestException as e:
        logging.error(f"A general API error occurred: {e}")
        raise
    
    # 7. ADDED: Catch unexpected Python crashes (non-API errors)
    except Exception as e:
        logging.exception("An unexpected system error occurred")
        raise
        

