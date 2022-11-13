import os
import boto3
from botocore.config import Config

def run():
    app_folder = os.environ.get('INPUT_APP-FOLDER')
    bucket_name = os.environ.get('INPUT_BUCKET-NAME')
    bucket_region = os.environ.get('INPUT_BUCKET-REGION')

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.client('s3', config=configuration)

    for root, dirs, files in os.walk(app_folder):
        for file in files:
            content_type = 'application/octet-stream'
            
            if file.endswith('.js'):
                content_type = 'application/javascript'
            elif file.endswith('.html'):
                content_type = 'text/html'
            elif file.endswith('.svg'):
                content_type = 'image/svg+xml'
            elif file.endswith('.css'):
                content_type = 'text/css'
            elif file.endswith('.png'):
                content_type = 'image/png'
        
            s3_client.upload_file(os.path.join(root, file), bucket_name, file, ExtraArgs={'ContentType': content_type})
    
    website_url = 'http://gh-actions-course.mariusmihai.org'
    print(f'"website-url={website_url}" >> $GITHUB_OUTPUTS')

if __name__ == "__main__":
    run()