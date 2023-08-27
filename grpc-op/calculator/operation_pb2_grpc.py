# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import operation_pb2 as operation__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Calculate = channel.unary_unary(
                '/Calculator/Calculate',
                request_serializer=operation__pb2.OperationRequest.SerializeToString,
                response_deserializer=operation__pb2.OperationResponse.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Calculate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Calculate': grpc.unary_unary_rpc_method_handler(
                    servicer.Calculate,
                    request_deserializer=operation__pb2.OperationRequest.FromString,
                    response_serializer=operation__pb2.OperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Calculate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Calculate',
            operation__pb2.OperationRequest.SerializeToString,
            operation__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)