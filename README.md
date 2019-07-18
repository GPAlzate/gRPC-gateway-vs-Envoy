<h1 align="center">Welcome to gRPC-gateway-vs-Envoy 👋</h1>
<p>
</p>

> A demo app that 1) compares the speed of proxies and 2) runs a demo for a simple microservice that is both HTTP/2.0+gRPC+proto3 and HTTP/1.0+REST+JSON compliant. 

## Usage

Make sure you have Python 3 and [Docker](https://www.docker.com/) installed. All other tools (PostgreSQL, Nginx) are used by pulling pre-built Docker images. Just run the following command in in the `gRPC-gateway-vs-Envoy/services` directory:

```sh
docker-compose up --build -d
```

There are two ways to run the demo app as a client.

#### 1) gRPC + Protocol Buffers over HTTP/2.0

Navigate to the `gRPC-gateway-vs-Envoy/services` directory and run:

```sh
python3 -m app.client
```

This runs a simple company recruiter CRUD app that writes to and reads from a PostgreSQL database.

#### 2) REST + JSON over HTTP/1.1

Coming soon!

## Author

👤 **Gabriel Alzate**

* Github: [@GPAlzate](https://github.com/GPAlzate)
