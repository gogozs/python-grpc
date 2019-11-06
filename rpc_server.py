from concurrent import futures
import time

import grpc

import ticket_pb2
import ticket_pb2_grpc
import datetime

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# ssh -p 58422 zhushen@42.159.107.199 -L 2222:10.2.0.45:22 -N

class Server(ticket_pb2_grpc.TrainServerServicer):
    # 工作函数
    def GetUserInfo(self, request, context):
        print("GetUserInfo request")
        return ticket_pb2.UserInfoResponse(
            passengers=[
                ticket_pb2.Passenger(name="张三", id_number="1234", type="成人", encode_str="jsdfsfqq", id_type="身份证"),
                ticket_pb2.Passenger(name="李四", id_number="2545", type="成人", encode_str="asewqwer", id_type="身份证"),
            ],
            code=0,
            msg="success"
        )

    def GetTrainInfo(self, request, context):
        print("GetTrainInfo request")
        return ticket_pb2.TrainResponse(
            code=0,
            msg="success",
            data=[
                ticket_pb2.TrainInfo(
                    train_number='G1',
                    start_time=datetime.datetime.now(),
                    end_time=datetime.datetime.now(),
                    duration=3600 * 3,
                    price=262.5,
                    ticket_remain={"二等座": "5", "一等座": "有"},
                    ticket_alternate={"二等座": True, "一等座": True},
                ),
                ticket_pb2.TrainInfo(
                    train_number='G2',
                    start_time=datetime.datetime.now(),
                    end_time=datetime.datetime.now(),
                    duration=3600 * 1,
                    price=362.5,
                    ticket_remain={"二等座": "有", "一等座": "有"},
                    ticket_alternate={"二等座": True, "一等座": True},
                ),
            ]
        )

    def Login(self, request, context):
        print("login request")
        if request.username == "zs":
            return ticket_pb2.UserInfoResponse(
                passengers=[
                    ticket_pb2.Passenger(name="张三", id_number="1234", type="成人", encode_str="jsdfsfqq", id_type="身份证"),
                    ticket_pb2.Passenger(name="李四", id_number="2545", type="成人", encode_str="asewqwer", id_type="身份证"),
                ],
                code=0,
                msg="success"
            )
        else:
            return ticket_pb2.UserInfoResponse(
                passengers=[
                ],
                code=1,
                msg="账号错误"
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
