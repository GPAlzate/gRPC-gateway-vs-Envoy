GATEWAY_FLAGS := -I.. -I$(GOPATH)/src \
					-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/ \
					-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

PYTHON_OUT := --python_out=.. --grpc_python_out=..

all:
	make proto
	make gostub
	make proxy
	make swagger

proto:
	python3 -m grpc_tools.protoc $(GATEWAY_FLAGS) $(PYTHON_OUT) ../proto/registration.proto

gostub:
	protoc $(GATEWAY_FLAGS) --go_out=plugins=grpc:../proxy ../proto/registration.proto 

proxy:
	protoc $(GATEWAY_FLAGS) --grpc-gateway_out=logtostderr=true:../proxy ../proto/registration.proto
	mv ../proxy/proto/* ../proxy
	rmdir ../proxy/proto
	cp -r ../proxy $(GOPATH)/src

swagger:
	protoc $(GATEWAY_FLAGS) --swagger_out=logtostderr=true:../swagger ../proto/registration.proto
	mv ../swagger/proto/* ../swagger
	rmdir ../swagger/proto

edits:
	vim -p Makefile client.py server.py ../

demo_list:
	http get :4747/students

demo_create:
	http post :4747/students/register id=12345678 name="'Paul Rivera'" dorm="'Kalibrr'"

demo_read:
	http get :4747/students/12345678

demo_update:
	http put :4747/students/update/12345678 changeDorm:='true' new="'Wig'"

demo_delete:
	http delete :4747/students/delete/12345678

