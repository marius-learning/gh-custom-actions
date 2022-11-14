FROM python:3.10-alpine3.16

# GitHub injects inputs as env variables
# ENV INPUT_APP-FOLDER
# ENV INPUT_BUCKET-NAME
# ENV INPUT_BUCKET-REGION

WORKDIR /home/app

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./ ./

CMD [ "python3", "/home/app/deployment.py" ]