# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ticket_pb2 as ticket__pb2


class TrainServerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
            "/ticket.TrainServer/Login",
            request_serializer=ticket__pb2.LoginRequest.SerializeToString,
            response_deserializer=ticket__pb2.UserInfoResponse.FromString,
        )
        self.GetUserInfo = channel.unary_unary(
            "/ticket.TrainServer/GetUserInfo",
            request_serializer=ticket__pb2.Empty.SerializeToString,
            response_deserializer=ticket__pb2.UserInfoResponse.FromString,
        )
        self.GetTrainInfo = channel.unary_unary(
            "/ticket.TrainServer/GetTrainInfo",
            request_serializer=ticket__pb2.TrainRequest.SerializeToString,
            response_deserializer=ticket__pb2.TrainResponse.FromString,
        )
        self.AddOrder = channel.unary_unary(
            "/ticket.TrainServer/AddOrder",
            request_serializer=ticket__pb2.OrderRequest.SerializeToString,
            response_deserializer=ticket__pb2.CommonResponse.FromString,
        )
        self.QueryOrder = channel.unary_unary(
            "/ticket.TrainServer/QueryOrder",
            request_serializer=ticket__pb2.CommonRequest.SerializeToString,
            response_deserializer=ticket__pb2.OrderResponse.FromString,
        )


class TrainServerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Login(self, request, context):
        """登录"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserInfo(self, request, context):
        """获取用户信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTrainInfo(self, request, context):
        """获取车次信息"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddOrder(self, request, context):
        """创建抢票订单"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def QueryOrder(self, request, context):
        """查询抢票订单"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TrainServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Login": grpc.unary_unary_rpc_method_handler(
            servicer.Login,
            request_deserializer=ticket__pb2.LoginRequest.FromString,
            response_serializer=ticket__pb2.UserInfoResponse.SerializeToString,
        ),
        "GetUserInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserInfo,
            request_deserializer=ticket__pb2.Empty.FromString,
            response_serializer=ticket__pb2.UserInfoResponse.SerializeToString,
        ),
        "GetTrainInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetTrainInfo,
            request_deserializer=ticket__pb2.TrainRequest.FromString,
            response_serializer=ticket__pb2.TrainResponse.SerializeToString,
        ),
        "AddOrder": grpc.unary_unary_rpc_method_handler(
            servicer.AddOrder,
            request_deserializer=ticket__pb2.OrderRequest.FromString,
            response_serializer=ticket__pb2.CommonResponse.SerializeToString,
        ),
        "QueryOrder": grpc.unary_unary_rpc_method_handler(
            servicer.QueryOrder,
            request_deserializer=ticket__pb2.CommonRequest.FromString,
            response_serializer=ticket__pb2.OrderResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ticket.TrainServer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
