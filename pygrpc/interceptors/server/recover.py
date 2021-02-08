from grpc_interceptor import ServerInterceptor
from typing import Any, Callable
import grpc
from grpc_interceptor.exceptions import GrpcException
import logging


class RecoverInterceptor(ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request: Any,
        context: grpc.ServicerContext,
        method_name: str,
    ) -> Any:
        try:
            return method(request, context)
        except GrpcException as e:
            context.set_code(e.status_code)
            context.set_details(e.details)
            raise e
        except Exception as e:
            logging.exception(e)
            raise e
