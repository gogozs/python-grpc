import time
from typing import Optional, Callable, Any, List, Union

import grpc
from grpc import Server
from concurrent import futures

from grpc import ServerInterceptor
import logging

default_interceptor_list: List[ServerInterceptor] = []
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
enable_graceful = True


def serve(
    name: str,
    target_server: Any,
    server_register: Callable[[Any, Server], None],
    port: int = 7070,
    interceptors: Optional[List[ServerInterceptor]] = None,
    max_workers: int = 100,
    secure: bool = False,
    key: str = "",
    crt: str = "",
    block: bool = True
):
    """
    :param name: 名称
    :param target_server: 实现类实例
    :param server_register: 注册function, find in xx_pb2_grpc.py like: add_XxServicer_to_server
    :param port: 端口
    :param interceptors: 拦截器
    :param max_workers: 并发数
    :param secure: enable ssl
    :param key: ssl key
    :param crt: ssl crt
    :param block: program need to be blocked or not
    :return:
    """
    if secure and (not key or not crt):
        raise Exception("invalid ssl conf")
    if interceptors is None:
        interceptors = default_interceptor_list

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=max_workers), interceptors=interceptors
    )
    server_register(target_server, server)
    if secure:
        with open(key, "rb") as f:
            private_key = f.read()
        with open(crt, "rb") as f:
            certificate_chain = f.read()
        server_credentials = grpc.ssl_server_credentials(
            (
                (
                    private_key,
                    certificate_chain,
                ),
            )
        )
        server.add_secure_port(f"[::]:{port}", server_credentials)
    else:
        server.add_insecure_port(f"[::]:{port}")

    server.start()  # start() 不会阻塞
    logging.info(f"{name} server start")
    
    if block:
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(grace=enable_graceful)
