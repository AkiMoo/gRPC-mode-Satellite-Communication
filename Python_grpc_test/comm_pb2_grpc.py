# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import comm_pb2 as comm__pb2


class CommStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transfer_CtoS = channel.stream_unary(
                '/Comm/Transfer_CtoS',
                request_serializer=comm__pb2.Request.SerializeToString,
                response_deserializer=comm__pb2.Reply.FromString,
                )
        self.Transfer_StoC = channel.unary_stream(
                '/Comm/Transfer_StoC',
                request_serializer=comm__pb2.Request.SerializeToString,
                response_deserializer=comm__pb2.Reply.FromString,
                )
        self.Transfer_Both = channel.stream_stream(
                '/Comm/Transfer_Both',
                request_serializer=comm__pb2.Request.SerializeToString,
                response_deserializer=comm__pb2.Reply.FromString,
                )


class CommServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transfer_CtoS(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transfer_StoC(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transfer_Both(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transfer_CtoS': grpc.stream_unary_rpc_method_handler(
                    servicer.Transfer_CtoS,
                    request_deserializer=comm__pb2.Request.FromString,
                    response_serializer=comm__pb2.Reply.SerializeToString,
            ),
            'Transfer_StoC': grpc.unary_stream_rpc_method_handler(
                    servicer.Transfer_StoC,
                    request_deserializer=comm__pb2.Request.FromString,
                    response_serializer=comm__pb2.Reply.SerializeToString,
            ),
            'Transfer_Both': grpc.stream_stream_rpc_method_handler(
                    servicer.Transfer_Both,
                    request_deserializer=comm__pb2.Request.FromString,
                    response_serializer=comm__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Comm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Comm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transfer_CtoS(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Comm/Transfer_CtoS',
            comm__pb2.Request.SerializeToString,
            comm__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Transfer_StoC(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Comm/Transfer_StoC',
            comm__pb2.Request.SerializeToString,
            comm__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Transfer_Both(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Comm/Transfer_Both',
            comm__pb2.Request.SerializeToString,
            comm__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
