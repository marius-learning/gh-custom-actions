FROM python:alpine

# RUN groupadd --gid 1000 app \
#     && useradd --uid 1000 --gid 1000 -m /home/app

# GitHub injects inputs as env variables
# ENV INPUT_APP-FOLDER
# ENV INPUT_BUCKET-NAME
# ENV INPUT_BUCKET-REGION

WORKDIR /home/app

COPY requirements.txt ./
# COPY --chown=app:app requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./ ./
# COPY --chown=app:app ./ ./

# USER app

CMD [ "python3", "/home/app/deployment.py" ]