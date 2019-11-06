from __future__ import print_function

import grpc

import ticket_pb2
import ticket_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = ticket_pb2_grpc.TrainServerStub(channel)
    response = stub.GetUserInfo(ticket_pb2.CommonRequest(username='zs'))
    print( response )


if __name__ == '__main__':
    run()
