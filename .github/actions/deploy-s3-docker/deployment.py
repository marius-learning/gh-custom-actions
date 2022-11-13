import os
import boto3
from botocose.config import Config

def run():
    app_folder = os.environ.get('INPUT_APP-FOLDER')
    bucket_name = os.environ.get('INPUT_BUCKET-NAME')
    bucket_region = os.environ.get('INPUT_BUCKET-REGION')

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.client('s3', config=configuration)

    for root, dirs, files in os.walk(app_folder):
        for file in files:
            s3_client.upload_file(os.path.join(root, file), bucket_name, file)
    
    website_url = 'http://gh-actions-course.mariusmihai.org'
    print(f'"website-rul={website_url}" >> $GITHUB_OUTPUTS')

if __name__ == "__main__":
    run()