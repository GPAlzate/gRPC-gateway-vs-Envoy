<h1 align="center">Welcome to gRPC-gateway-vs-Envoy 👋</h1>
<p>
</p>

> A demo app that 1) compares the speed of proxies and 2) runs a demo for a simple microservice that is both HTTP/2.0+gRPC+proto3 and HTTP/1.0+REST+JSON compliant. 

## Usage

Usage commands will take place in the `gRPC-gateway-vs-Envoy/services` directory. Make sure you have Python 3 installed. To run the gRPC client app, install the necessary packages in the `requirements.txt` file:

```sh
pip3 install -r requirements.txt
```

Note: psycopg2 isn't required for the client app but it is for the server app. You can refrain from downloading this if you want, and simply run `pip3 install` on the other packages specified in the `requirements.txt` file manually.

Also make sure you [Docker](https://www.docker.com/) installed. All other tools (PostgreSQL, Nginx) are used by pulling pre-built Docker images. Just run the following command in in the `gRPC-gateway-vs-Envoy/services` directory:

```sh
docker-compose up --build -d
```

At this point, there are 4 docker containers running: 1) one for the python server, 2) the PostgreSQL database, 3) the envoy proxy, and 4) the nginx proxy/load balancer.

There are two ways to run the demo app as a client.

#### 1) gRPC + Protocol Buffers over HTTP/2.0

Navigate to the `gRPC-gateway-vs-Envoy/services` directory and run:

```sh
python3 -m app.client
```

This runs a simple company recruiter CRUD app that writes to and reads from a PostgreSQL database.

#### 2) REST + JSON over HTTP/1.1

Sorry for the inconvenience, but the best way to test the REST API specified by the proto file for now is through the command line. I recommend using [HTTPie](https://httpie.org/) by running `pip3 install httpie`, but you can use curl if you're more comfortable with it.

When sending strings in a POST body, single quotes `''` are necessary. When using `curl`, these can be included by using the backslash escape by typing `''\'`. This is not necessary with HTTPie.

You can optionally pipe the curl response to `json_pp` to output the response in a readable format.

Examples:

```sh
#This gets a company from the database

#GET using curl:
curl http://localhost:4748/companies/42474679 | json_pp

#GET using httpie
http :4748/companies/42474679
```

```sh
#This adds a new company

#POST using curl (look at all those backslashes and single quotes!):
curl -d '{"companyCode":987654321, "companyName":"'\''Kalibrr'\''", "numOpenings":1, "isBrokerage":false}' -X POST http://localhost:4748/register | json_pp

#POST using httpie
http post :4748/register companyCode=987654321 companyName="'Kalibrr'" numOpenings=1 isBrokerage:=false
```

## Author

👤 **Gabriel Alzate**

* Github: [@GPAlzate](https://github.com/GPAlzate)

