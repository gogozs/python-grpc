import time
from typing import Callable, Any

import grpc
from grpc_interceptor import ServerInterceptor
import logging


class LoggerInterceptor(ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
        start_at = time.time()
        logging.debug(f"request: {request}")
        res = method(request, context)
        end_at = time.time()
        logging.debug(f"response: {res}")
        logging.info(f"{method_name} run success in {end_at-start_at}s")
        return res
