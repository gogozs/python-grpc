from __future__ import print_function

import ticket_pb2
import ticket_pb2_grpc
from pygrpc.client import Runner


def run():
    with Runner("localhost:50051", ticket_pb2_grpc.TrainServerStub) as stub:
        response = stub.GetUserInfo(ticket_pb2.CommonRequest(username="zs"))
        print(response)


if __name__ == "__main__":
    run()
