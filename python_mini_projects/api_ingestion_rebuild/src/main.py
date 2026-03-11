import logging , sys
from api_client import fetch_api_data
from validation import validation_schema
from loader import load_to_postgres



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s | %(filename)s | %(lineno)d",
    handlers=[
        logging.FileHandler("api_log.log"),   
        logging.StreamHandler(sys.stdout)      
   ]
)



def run_pipeline():
    logging.info("Pipeline has been initiated")
    datas=fetch_api_data()
    logging.info("data successfully fetched")
    validated_data=validation_schema(datas)
    logging.info("data validation completed")
    load_to_postgres(validated_data)
    logging.info("data loading completed")


if __name__=="__main__":
    run_pipeline()