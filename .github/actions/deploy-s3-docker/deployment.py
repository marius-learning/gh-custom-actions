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
            content_type = get_content_type(extension)
            s3_client.upload_file(os.path.join(root, file), bucket_name, file, ExtraArgs={'ContentType': content_type})
    
    website_url_r53 = 'http://gh-actions-course.mariusmihai.org'
    website_url_s3 = 'http://gh-actions-course.mariusmihai.org.s3-website.us-east-1.amazonaws.com'

    # New solution
    with open(os.environ.get('GITHUB_OUTPUT'), 'a') as output:
        print(f'website-url-s3={website_url_s3}', file=output)
        print(f'website-url-r53={website_url_r53}', file=output)

    # Old solution
    # print(f'::set-output name=website-url-r53::{website_url_r53}')
    # print(f'::set-output name=website-url-s3::{website_url_s3}')

if __name__ == "__main__":
    run()