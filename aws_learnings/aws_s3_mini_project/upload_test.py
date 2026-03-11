import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


class S3Injestor:
    def __init__(self):
        """
          initializes the S# client using environment variables
        """
        self.bucket=os.getenv('BUCKET_NAME')

        # Using a session 
        self.session  = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION'))
        self.s3=self.session.client('s3')
    def upload_file(self,local_file_path:str,s3_key:str):
        """
        Uploads a file to s3.
        local_file_path: The path to the file on your computer.
        s3_key: The 'path' inside the S3 bucket('bronze/data.csv').
        """
        # Convert string path to a Path object
        path = Path(local_file_path)

        if not path.exists():
            print(f"Error : The file{Path} does not exists locally.")
            return
        
        try:
            print(f"ingesting {path.name} to s3://{self.bucket}/{s3_key}....")

            # Extra Check : In production , we use ExtraArgs for things like Encryption
            self.s3.upload_file(
            str(path),
            self.bucket,
            s3_key,
            ExtraArgs={'ServerSideEncryption': 'AES256'})

        except ClientError as e:
            print(f"AWS client Error: {e}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")    

if __name__ == "__main__":
    # Initialize our Injestor class
    ingestor = S3Injestor()
    
    # Run the test
    ingestor.upload_file('test_data.csv', 'bronze/raw_github_data.csv')


            
         
  
     
        
