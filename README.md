## python grpc

### install
```
pip install grpcio
pip install grpcio-tools
```

### usage
```
python -m grpc.tools.protoc -I=. --python_out=./ --grpc_python_out=./ ticket.proto
```