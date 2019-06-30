INCLUDE_FLAGS := -I/usr/local/include -I.. \
					--include_imports --include_source_info \
					-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis

OUTPUT := --python_out=.. --grpc_python_out=.. --descriptor_set_out=../proto/registration.pb

all:
	make proto

proto:
	python3 -m grpc_tools.protoc $(INCLUDE_FLAGS) $(OUTPUT) ../proto/registration.proto

edits:
	vim -p ../{*.yaml,Dockerfile*} client.py server.py

demo_list:
	http get :4748/students

demo_create:
	http post :4748/students/register id=12345678 name="'Paul Rivera'" dorm="'Kalibrr'"

demo_read:
	http get :4748/students/12345678

demo_update:
	http put :4748/students/update/12345678 changeDorm=true new="'Silicon Valley'"

demo_delete:
	http delete :4748/students/delete/12345678

