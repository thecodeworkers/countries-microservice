# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import state_pb2 as state__pb2


class StateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.table = channel.unary_unary(
                '/State/table',
                request_serializer=state__pb2.StateTableRequest.SerializeToString,
                response_deserializer=state__pb2.StateTableResponse.FromString,
                )
        self.get_all = channel.unary_unary(
                '/State/get_all',
                request_serializer=state__pb2.StateEmpty.SerializeToString,
                response_deserializer=state__pb2.StateMultipleResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/State/get',
                request_serializer=state__pb2.StateIdRequest.SerializeToString,
                response_deserializer=state__pb2.StateResponse.FromString,
                )
        self.save = channel.unary_unary(
                '/State/save',
                request_serializer=state__pb2.StateNotIdRequest.SerializeToString,
                response_deserializer=state__pb2.StateResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/State/update',
                request_serializer=state__pb2.StateRequest.SerializeToString,
                response_deserializer=state__pb2.StateResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/State/delete',
                request_serializer=state__pb2.StateIdRequest.SerializeToString,
                response_deserializer=state__pb2.StateEmpty.FromString,
                )


class StateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'table': grpc.unary_unary_rpc_method_handler(
                    servicer.table,
                    request_deserializer=state__pb2.StateTableRequest.FromString,
                    response_serializer=state__pb2.StateTableResponse.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=state__pb2.StateEmpty.FromString,
                    response_serializer=state__pb2.StateMultipleResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=state__pb2.StateIdRequest.FromString,
                    response_serializer=state__pb2.StateResponse.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=state__pb2.StateNotIdRequest.FromString,
                    response_serializer=state__pb2.StateResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=state__pb2.StateRequest.FromString,
                    response_serializer=state__pb2.StateResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=state__pb2.StateIdRequest.FromString,
                    response_serializer=state__pb2.StateEmpty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'State', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class State(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/table',
            state__pb2.StateTableRequest.SerializeToString,
            state__pb2.StateTableResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/get_all',
            state__pb2.StateEmpty.SerializeToString,
            state__pb2.StateMultipleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/get',
            state__pb2.StateIdRequest.SerializeToString,
            state__pb2.StateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/save',
            state__pb2.StateNotIdRequest.SerializeToString,
            state__pb2.StateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/update',
            state__pb2.StateRequest.SerializeToString,
            state__pb2.StateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/State/delete',
            state__pb2.StateIdRequest.SerializeToString,
            state__pb2.StateEmpty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
