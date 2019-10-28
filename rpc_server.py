from concurrent import futures
import time

import grpc


import ticket_pb2
import ticket_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Server(ticket_pb2_grpc.TrainServerServicer):
    # 工作函数
    def GetUserInfo(self, request, context):
        return ticket_pb2.UserInfoResponse(
            passengers = [
                ticket_pb2.Passenger(name="张三", id_number="1234", type="成人"),
                ticket_pb2.Passenger(name="李四", id_number="2545", type="成人"),
            ],
            code = 100,
            msg = "asdfs"
        )


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_pb2_grpc.add_TrainServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
