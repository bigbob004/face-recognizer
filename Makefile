generate:
	python3 -m grpc_tools.protoc -I protobuf --python_out=. --pyi_out=. --grpc_python_out=. protobuf/face_recognizer_api.proto