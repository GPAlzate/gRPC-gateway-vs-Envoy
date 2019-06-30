FROM python:3.7-slim-stretch

# Set the working directory to /app
WORKDIR /housing
COPY . /housing

# install requirements
RUN pip3 install -r requirements.txt

EXPOSE 50051

CMD ["python", "-u", "-m" ,"app.server"]
