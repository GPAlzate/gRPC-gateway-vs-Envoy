INCLUDE_FLAGS := -I/usr/local/include -I.. \
					--include_imports --include_source_info \
					-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

DOCS := -I. -I/Users/GabeAlzate/go/src/ \
			-I/Users/GabeAlzate/go/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
			--plugin=protoc-gen-doc=/Users/GabeAlzate/go/bin/protoc-gen-doc \


OUTPUT := --python_out=.. --grpc_python_out=.. --descriptor_set_out=../proto/registration.pb

all:
	make proto
	make docs

proto:
	python3 -m grpc_tools.protoc $(INCLUDE_FLAGS) $(OUTPUT) ../proto/registration.proto

edits:
	vim -p ../{*.yaml,Dockerfile*} client.py server.py

docs:
	protoc $(DOCS) --doc_out=.. --doc_opt=markdown,README.md proto/registration.proto 


demo_list:
	http get :4748/students

demo_create:
	http post :4748/students/register id=12345678 name="'Paul Rivera'" dorm="'Kalibrr'"

demo_read:
	http get :4748/students/12345678

demo_update:
	http put :4748/students/update/12345678 changeDorm=1 new="'Silicon Valley'"

demo_delete:
	http delete :4748/students/delete/12345678

