from __future__ import print_function
import grpc
from grpc import (
    Channel,
    StreamStreamClientInterceptor,
    StreamUnaryClientInterceptor,
    UnaryStreamClientInterceptor,
    UnaryUnaryClientInterceptor,
)
from typing import Optional, Callable, List, Union, Any

type_client_inspectors = Optional[
    List[
        Union[
            StreamStreamClientInterceptor,
            StreamUnaryClientInterceptor,
            UnaryStreamClientInterceptor,
            UnaryUnaryClientInterceptor,
        ]
    ]
]
default_interceptors: type_client_inspectors = []


class Runner(object):
    def __init__(
        self,
        uri: str,
        stub_func,
        interceptors: type_client_inspectors = None,
        secure: bool = False,
        crt: str = None,
    ):
        """client runner
        :param uri: grpc server uri
        :param stub_func: find in xx_pb2_grpc.py like XxServerStub
        :param interceptors:
        :param secure: if true run with ssl
        :param crt: ssl key
        
        sample:
        >>> with Runner("localhost:50051", ticket_pb2_grpc.TrainServerStub) as stub:
        >>>      response = stub.GetUserInfo(ticket_pb2.CommonRequest(username="zs"))
        >>>      print(response)

        """
        self._channel: Optional[Channel] = None
        self._stub: Any = None
        if not interceptors:
            interceptors = default_interceptors
        if secure and not crt:
            raise Exception("secure mode need crt")
        if secure:
            self._run_secure(uri, crt, interceptors, stub_func)
        else:
            self._run_insecure(uri, interceptors, stub_func)

    def __enter__(self):
        return self._stub

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()
        return False

    def _close(self):
        self._channel.close()

    def _run_secure(
        self,
        uri: str,
        crt: str,
        interceptors: type_client_inspectors,
        register,
    ):
        with open(crt, "rb") as f:
            credentials = grpc.ssl_channel_credentials(f.read())
        self._channel = grpc.secure_channel(uri, credentials)
        self._channel = grpc.intercept_channel(self._channel, *interceptors)
        self._stub = register(self._channel)

    def _run_insecure(self, uri: str, interceptors, register: Callable[[Channel], None]):
        self._channel = grpc.intercept_channel(
            grpc.insecure_channel(uri), *interceptors
        )
        self._stub = register(self._channel)
        self._channel = self._channel
