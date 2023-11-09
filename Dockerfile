# our base image
FROM python:alpine

# Install python and pip
RUN apk add --no-cache python3 py3-pip
RUN python3 -m pip install -U pip

RUN pip3 install psycopg2-binary

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY . /usr/src/app/
RUN echo "dir after copy"
RUN ls -la

# add env vars
RUN source /usr/src/app/env.sh
# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/run.py"]
