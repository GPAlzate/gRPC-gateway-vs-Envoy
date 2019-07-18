package main;

import (
    "context"  // Use "golang.org/x/net/context" for Golang version <= 1.6
    "flag"
    "net/http"

    "github.com/golang/glog"
    "github.com/grpc-ecosystem/grpc-gateway/runtime"
    "google.golang.org/grpc"

    gw "proxy_stubs"  // Update
)

var (
    // command-line options:
    // gRPC server endpoint
    deleteEndpoint = flag.String("endpoint",  "0.0.0.0:50051", "gRPC server endpoint")
)

func runDelete() error {
    ctx := context.Background()
    ctx, cancel := context.WithCancel(ctx)
    defer cancel()

    // Register gRPC server endpoint
    // Note: Make sure the gRPC server is running properly and accessible
    mux := runtime.NewServeMux()
    opts := []grpc.DialOption{grpc.WithInsecure()}
    err := gw.RegisterRecruiterHandlerFromEndpoint(ctx, mux,  *deleteEndpoint, opts)
    if err != nil {
        return err
    }

    // Start HTTP server (and proxy calls to gRPC server endpoint)
    return http.ListenAndServe(":4753", mux)
}

func main() {
    flag.Parse()
    defer glog.Flush()

    if err := runDelete(); err != nil {
        glog.Fatal(err)
    }
}
