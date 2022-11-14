import os
import boto3
from botocore.config import Config

def get_content_type(extension):
    match extension:
        case '.js':
            content_type = 'application/javascript'
        case '.html':
            content_type = 'text/html'
        case '.svg':
            content_type = 'image/svg+xml'
        case '.css':
            content_type = 'text/css'
        case '.png':
            content_type = 'image/png'
        case _ :
            content_type = 'application/octet-stream'

    return content_type

def run():
    app_folder = os.environ.get('INPUT_APP-FOLDER')
    bucket_name = os.environ.get('INPUT_BUCKET-NAME')
    bucket_region = os.environ.get('INPUT_BUCKET-REGION')

    configuration = Config(region_name=bucket_region)

    s3_client = boto3.client('s3', config=configuration)

    for root, dirs, files in os.walk(app_folder):
        for file in files:
            name, extension = os.path.splitext(file)
            content_type = get_content_type('')
            s3_client.upload_file(os.path.join(root, file), bucket_name, file, ExtraArgs={'ContentType': content_type})
    
    website_url_r53 = 'http://gh-actions-course.mariusmihai.org'
    print(f'"website-url-r53={website_url_r53}" >> $GITHUB_OUTPUTS')

    website_url_s3 = 'http://gh-actions-course.mariusmihai.org.s3-website.us-east-1.amazonaws.com'
    print(f'"website-url-s3=%{website_url_s3}" >> $GITHUB_OUTPUTS')

if __name__ == "__main__":
    run()