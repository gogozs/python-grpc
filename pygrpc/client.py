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
        register,
        interceptors: type_client_inspectors = None,
        secure: bool = False,
        crt: str = None,
    ):
        self._channel: Optional[Channel] = None
        self._stub: Any = None
        if not interceptors:
            interceptors = default_interceptors
        if secure and not crt:
            raise Exception("secure mode need crt")
        if secure:
            self.run_secure(uri, crt, interceptors, register)
        else:
            self.run_insecure(uri, interceptors, register)

    def __enter__(self):
        return self._stub

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()
        return False

    def _close(self):
        self._channel.close()

    def run_secure(
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

    def run_insecure(self, uri: str, interceptors, register: Callable[[Channel], None]):
        self._channel = grpc.intercept_channel(
            grpc.insecure_channel(uri), *interceptors
        )
        self._stub = register(self._channel)
        self._channel = self._channel
