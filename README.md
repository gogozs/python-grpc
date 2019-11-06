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


### 状态码
> 参考 [grpc状态码](https://skyao.io/learning-grpc/server/status/status_code_definition.html)