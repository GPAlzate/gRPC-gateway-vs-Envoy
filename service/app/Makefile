BINARY_FLAGS := --include_imports --include_source_info

GRPC_FLAGS := -I.. -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/ \
					-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

OUTPUT := --python_out=.. --grpc_python_out=.. --descriptor_set_out=../proto/recruiter.pb

PROTO := ../proto/recruiter.proto

all: $(PROTO)
	make proto
	make gostub
	make swagger
	make docs

proto: $(PROTO)
	python3 -m grpc_tools.protoc $(GRPC_FLAGS) $(BINARY_FLAGS) \
			$(OUTPUT) $(PROTO)

gostub: $(PROTO)
	protoc $(GRPC_FLAGS) \
			--go_out=plugins=grpc:../proxy_stubs \
			--grpc-gateway_out=logtostderr=true:../proxy_stubs $(PROTO);
	mv ../proxy_stubs/proto/* ../proxy_stubs;
	rmdir ../proxy_stubs/proto;
	cp -r ../proxy_stubs $(GOPATH)/src;

swagger: $(PROTO)
	protoc $(GRPC_FLAGS) --swagger_out=logtostderr=true:../swagger $(PROTO);
	mv ../swagger/proto/* ../swagger;
	rmdir ../swagger/proto;

docs:
	protoc $(GRPC_FLAGS) --doc_out=../.. --doc_opt=html,index.html ../proto/recruiter.proto;

clean:
	rm ../proto/{recruiter*,recruiter.pb};
	rm ../proxy_stubs/*;
	rm ../swagger/*;
