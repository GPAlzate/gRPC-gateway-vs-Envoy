DOCS := -I. -I/Users/GabeAlzate/go/src/ \
			-I/Users/GabeAlzate/go/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
			--plugin=protoc-gen-doc=/Users/GabeAlzate/go/bin/protoc-gen-doc \

docs:
	protoc $(DOCS) --doc_out=.. --doc_opt=markdown,README.md proto/registration.proto 
	protoc $(DOCS) --doc_out=.. --doc_opt=html,index.html proto/registration.proto 
