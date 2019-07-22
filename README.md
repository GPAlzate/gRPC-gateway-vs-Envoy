<h1 align="center">Welcome to gRPC-gateway-vs-Envoy 👋</h1>
<p>
</p>

> A demo app that 1) compares the speed of proxies and 2) runs a demo for a simple microservice that is both HTTP/2.0+gRPC+proto3 and HTTP/1.0+REST+JSON compliant. 

## Usage

Usage commands will take place in the `gRPC-gateway-vs-Envoy/service` directory. Make sure you have Python 3 installed. To run the gRPC client app, install the necessary packages in the `requirements.txt` file:

```sh
pip3 install -r requirements.txt
```

Note: psycopg2 isn't required for the client app but it is for the server app. You can refrain from downloading this if you want, and simply run `pip3 install` on the other packages specified in the `requirements.txt` file manually.

Also make sure you [Docker](https://www.docker.com/) installed. All other tools (PostgreSQL, Nginx) are used by pulling pre-built Docker images. Just run the following command in in the `gRPC-gateway-vs-Envoy/service` directory:

```sh
docker-compose up --build -d
```

At this point, there are four docker containers running: one for the
1. python server,
2. PostgreSQL database,
3. the envoy proxy, and
4. the nginx proxy/load balancer.

There are two ways to run the demo client app through the command line:

#### 1) gRPC + Protocol Buffers over HTTP/2.0

Navigate to the `gRPC-gateway-vs-Envoy/service` directory and run:

```sh
python3 -m app.client
```

This runs a simple company recruiter CRUD app that writes to and reads from a PostgreSQL database. Simply follow the instructions to play around with how it should work. You can also optionally use [BloomRPC](https://github.com/uw-labs/bloomrpc), a GUI client for gRPC services, to send requests quickly.

#### 2) REST + JSON over HTTP/1.1

Sorry for the inconvenience, but the best way to test the REST API specified by the proto file for now is through the command line. I recommend using [HTTPie](https://httpie.org/) by running `pip3 install httpie`, but you can use curl if you're more comfortable with it.

When sending strings in a POST body, single quotes `''` are necessary. When using `curl`, these can be included by using the backslash escape by typing `''\'`. This is not necessary with HTTPie.

You can optionally pipe the curl response to `json_pp` to output the response in a readable format.

Examples:

```sh
#This gets a company from the database

#GET using curl:
curl http://localhost:4748/companies/42474679 | json_pp

#GET using httpie; no address defaults to localhost
http :4748/companies/42474679
```

```sh
#This adds a new company

#POST using curl (look at all those backslashes and single quotes!): -->
curl -d '{"companyCode":987654321, "companyName":"'\''Kalibrr'\''", "numOpenings":1, "isBrokerage":false}' -X POST http://localhost:4748/register | json_pp

#POST using httpie
http post :4748/register companyCode=987654321 companyName="'Kalibrr'" numOpenings=1 isBrokerage:=false
```

## Proxies (WORK IN PROGRESS)

`4748` is the port number of the Envoy proxy server. However, multiple Go servers were created for testing purposes as well because testsshowed that Envoy is apparently sub-optimal. Previous load testing using [Locustio](https://locust.io/) showed that a setup of Go proxy servers load-balanced with Nginx was the best system to proxy JSON over HTTP/1.1 requests to the main gRPC server.

However, upon recently testing with [hey](https://github.com/rakyll/hey), apparently that's not the case. Thus, further testing has to be done with regards to optimizing the proxy servers. If you'd like to test, feel free to install [Golang](https://golang.org/) and run the servers in the `go_servers` directory.

I'm unfamiliar with go, so I currently run the Go servers the only way I know how: 4 tabs, one proxy server per tab, run with the command `go run [name].go`. The Nginx proxy sends requests to these Go proxies, so once the docker containers are running, send all http requests to `http://localhost:8080/`, the port on which Nginx is listening.

Or, you can just scrap Nginx entirely and/or just use one proxy server and send HTTP requests to that one. The proxy servers get.go, post.go, put.go, delete.go listen on ports 4747, 4749, 4751, 4753, respectively.

## Improvements

If you'd like to explore protobufs and gRPC, simply go to the `app` directory and run `make`. Before doing so, __you must also install go and install [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway)__. Afterwards, set your `$GOPATH` with:

```sh
export PATH=$PATH:/usr/local/go/bin
export GOPATH=~/go
source ~/.profile
```

#### To-do list:
[] Learn how running Go files works so that I can Dockerize the Go server(s)
[] Run tests to determine the best proxy server system

## Author

👤 **Gabriel Alzate**

* Github: [@GPAlzate](https://github.com/GPAlzate)

