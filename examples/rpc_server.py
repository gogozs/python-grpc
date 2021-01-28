import ticket_pb2
import ticket_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Server(ticket_pb2_grpc.TrainServerServicer):
    # 工作函数
    def GetUserInfo(self, request, context):
        print("GetUserInfo request")
        return ticket_pb2.UserInfoResponse(
            passengers=[
                ticket_pb2.Passenger(
                    name="张三",
                    id_number="1234",
                    type="成人",
                    encode_str="jsdfsfqq",
                    id_type="身份证",
                ),
                ticket_pb2.Passenger(
                    name="李四",
                    id_number="2545",
                    type="成人",
                    encode_str="asewqwer",
                    id_type="身份证",
                ),
            ],
            code=0,
            msg="success",
        )

    def GetTrainInfo(self, request, context):
        print("GetTrainInfo request")
        return ticket_pb2.TrainResponse(
            code=0,
            msg="success",
            data=[
                ticket_pb2.TrainInfo(
                    train_number="G1",
                    start_time=Timestamp(),
                    end_time=Timestamp(),
                    duration=3600 * 3,
                    price=262.5,
                    ticket_remain={"二等座": "5", "一等座": "有"},
                    ticket_alternate={"二等座": True, "一等座": True},
                ),
                ticket_pb2.TrainInfo(
                    train_number="G2",
                    start_time=Timestamp(),
                    end_time=Timestamp(),
                    duration=3600 * 1,
                    price=362.5,
                    ticket_remain={"二等座": "有", "一等座": "有"},
                    ticket_alternate={"二等座": True, "一等座": True},
                ),
            ],
        )

    def Login(self, request, context):
        print("login request")
        if request.username == "zs":
            return ticket_pb2.UserInfoResponse(
                passengers=[
                    ticket_pb2.Passenger(
                        name="张三",
                        id_number="1234",
                        type="成人",
                        encode_str="jsdfsfqq",
                        id_type="身份证",
                    ),
                    ticket_pb2.Passenger(
                        name="李四",
                        id_number="2545",
                        type="成人",
                        encode_str="asewqwer",
                        id_type="身份证",
                    ),
                ],
                code=0,
                msg="success",
            )
        else:
            return ticket_pb2.UserInfoResponse(passengers=[], code=1, msg="账号错误")


def serve(port: int = 50051):
    from pygrpc.server import serve

    serve(
        "",
        Server(),
        ticket_pb2_grpc.add_TrainServerServicer_to_server,
        port,
        max_workers=100,
    )


if __name__ == "__main__":
    serve()
