# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bragi_schema.bragi import bragi_pb2 as bragi_dot_bragi__pb2


class BragiGrpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sports = channel.unary_unary(
                '/bragi.BragiGrpc/Sports',
                request_serializer=bragi_dot_bragi__pb2.SportsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.SportsResponse.FromString,
                )
        self.Tournaments = channel.unary_unary(
                '/bragi.BragiGrpc/Tournaments',
                request_serializer=bragi_dot_bragi__pb2.TournamentsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.TournamentResponse.FromString,
                )
        self.TournamentInfo = channel.unary_unary(
                '/bragi.BragiGrpc/TournamentInfo',
                request_serializer=bragi_dot_bragi__pb2.TournamentInfoRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.TournamentInfoResponse.FromString,
                )
        self.TeamHistoricalStatistics = channel.unary_unary(
                '/bragi.BragiGrpc/TeamHistoricalStatistics',
                request_serializer=bragi_dot_bragi__pb2.TeamHistoricalStatisticsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.HistoricalStatisticsResponse.FromString,
                )
        self.LastFiveEncounters = channel.unary_unary(
                '/bragi.BragiGrpc/LastFiveEncounters',
                request_serializer=bragi_dot_bragi__pb2.LastFiveEncountersRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.LastFiveEncountersResponse.FromString,
                )
        self.PostMapStatistics = channel.unary_unary(
                '/bragi.BragiGrpc/PostMapStatistics',
                request_serializer=bragi_dot_bragi__pb2.PostMapStatisticsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.PostMapStatisticsResponse.FromString,
                )
        self.TournamentStatistics = channel.unary_unary(
                '/bragi.BragiGrpc/TournamentStatistics',
                request_serializer=bragi_dot_bragi__pb2.TournamentStatisticsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.TournamentStatisticsResponse.FromString,
                )
        self.TeamTournamentStatistics = channel.unary_unary(
                '/bragi.BragiGrpc/TeamTournamentStatistics',
                request_serializer=bragi_dot_bragi__pb2.TeamTournamentStatisticsRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.TeamTournamentStatisticsResponse.FromString,
                )
        self.PlayerStatisticsAccordingRole = channel.unary_unary(
                '/bragi.BragiGrpc/PlayerStatisticsAccordingRole',
                request_serializer=bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleResponse.FromString,
                )
        self.Csgo2dMaFeed = channel.unary_stream(
                '/bragi.BragiGrpc/Csgo2dMaFeed',
                request_serializer=bragi_dot_bragi__pb2.Csgo2dMaFeedRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.Csgo2dMap.FromString,
                )
        self.CsgoScoreBoardFeed = channel.unary_stream(
                '/bragi.BragiGrpc/CsgoScoreBoardFeed',
                request_serializer=bragi_dot_bragi__pb2.CsgoScoreBoardFeedRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.CsgoScoreBoard.FromString,
                )
        self.CsgoEventsFeed = channel.unary_stream(
                '/bragi.BragiGrpc/CsgoEventsFeed',
                request_serializer=bragi_dot_bragi__pb2.CsgoEventsFeedRequest.SerializeToString,
                response_deserializer=bragi_dot_bragi__pb2.CsgoEvents.FromString,
                )


class BragiGrpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Sports(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tournaments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TournamentInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TeamHistoricalStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastFiveEncounters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostMapStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TournamentStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TeamTournamentStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerStatisticsAccordingRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Csgo2dMaFeed(self, request, context):
        """streamed ----------------------------------------------------------------------------------------------------------

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CsgoScoreBoardFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CsgoEventsFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BragiGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sports': grpc.unary_unary_rpc_method_handler(
                    servicer.Sports,
                    request_deserializer=bragi_dot_bragi__pb2.SportsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.SportsResponse.SerializeToString,
            ),
            'Tournaments': grpc.unary_unary_rpc_method_handler(
                    servicer.Tournaments,
                    request_deserializer=bragi_dot_bragi__pb2.TournamentsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.TournamentResponse.SerializeToString,
            ),
            'TournamentInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.TournamentInfo,
                    request_deserializer=bragi_dot_bragi__pb2.TournamentInfoRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.TournamentInfoResponse.SerializeToString,
            ),
            'TeamHistoricalStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.TeamHistoricalStatistics,
                    request_deserializer=bragi_dot_bragi__pb2.TeamHistoricalStatisticsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.HistoricalStatisticsResponse.SerializeToString,
            ),
            'LastFiveEncounters': grpc.unary_unary_rpc_method_handler(
                    servicer.LastFiveEncounters,
                    request_deserializer=bragi_dot_bragi__pb2.LastFiveEncountersRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.LastFiveEncountersResponse.SerializeToString,
            ),
            'PostMapStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.PostMapStatistics,
                    request_deserializer=bragi_dot_bragi__pb2.PostMapStatisticsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.PostMapStatisticsResponse.SerializeToString,
            ),
            'TournamentStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.TournamentStatistics,
                    request_deserializer=bragi_dot_bragi__pb2.TournamentStatisticsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.TournamentStatisticsResponse.SerializeToString,
            ),
            'TeamTournamentStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.TeamTournamentStatistics,
                    request_deserializer=bragi_dot_bragi__pb2.TeamTournamentStatisticsRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.TeamTournamentStatisticsResponse.SerializeToString,
            ),
            'PlayerStatisticsAccordingRole': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayerStatisticsAccordingRole,
                    request_deserializer=bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleResponse.SerializeToString,
            ),
            'Csgo2dMaFeed': grpc.unary_stream_rpc_method_handler(
                    servicer.Csgo2dMaFeed,
                    request_deserializer=bragi_dot_bragi__pb2.Csgo2dMaFeedRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.Csgo2dMap.SerializeToString,
            ),
            'CsgoScoreBoardFeed': grpc.unary_stream_rpc_method_handler(
                    servicer.CsgoScoreBoardFeed,
                    request_deserializer=bragi_dot_bragi__pb2.CsgoScoreBoardFeedRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.CsgoScoreBoard.SerializeToString,
            ),
            'CsgoEventsFeed': grpc.unary_stream_rpc_method_handler(
                    servicer.CsgoEventsFeed,
                    request_deserializer=bragi_dot_bragi__pb2.CsgoEventsFeedRequest.FromString,
                    response_serializer=bragi_dot_bragi__pb2.CsgoEvents.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bragi.BragiGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BragiGrpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Sports(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/Sports',
            bragi_dot_bragi__pb2.SportsRequest.SerializeToString,
            bragi_dot_bragi__pb2.SportsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Tournaments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/Tournaments',
            bragi_dot_bragi__pb2.TournamentsRequest.SerializeToString,
            bragi_dot_bragi__pb2.TournamentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TournamentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/TournamentInfo',
            bragi_dot_bragi__pb2.TournamentInfoRequest.SerializeToString,
            bragi_dot_bragi__pb2.TournamentInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TeamHistoricalStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/TeamHistoricalStatistics',
            bragi_dot_bragi__pb2.TeamHistoricalStatisticsRequest.SerializeToString,
            bragi_dot_bragi__pb2.HistoricalStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastFiveEncounters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/LastFiveEncounters',
            bragi_dot_bragi__pb2.LastFiveEncountersRequest.SerializeToString,
            bragi_dot_bragi__pb2.LastFiveEncountersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostMapStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/PostMapStatistics',
            bragi_dot_bragi__pb2.PostMapStatisticsRequest.SerializeToString,
            bragi_dot_bragi__pb2.PostMapStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TournamentStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/TournamentStatistics',
            bragi_dot_bragi__pb2.TournamentStatisticsRequest.SerializeToString,
            bragi_dot_bragi__pb2.TournamentStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TeamTournamentStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/TeamTournamentStatistics',
            bragi_dot_bragi__pb2.TeamTournamentStatisticsRequest.SerializeToString,
            bragi_dot_bragi__pb2.TeamTournamentStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerStatisticsAccordingRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bragi.BragiGrpc/PlayerStatisticsAccordingRole',
            bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleRequest.SerializeToString,
            bragi_dot_bragi__pb2.PlayerStatisticsAccordingRoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Csgo2dMaFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bragi.BragiGrpc/Csgo2dMaFeed',
            bragi_dot_bragi__pb2.Csgo2dMaFeedRequest.SerializeToString,
            bragi_dot_bragi__pb2.Csgo2dMap.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CsgoScoreBoardFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bragi.BragiGrpc/CsgoScoreBoardFeed',
            bragi_dot_bragi__pb2.CsgoScoreBoardFeedRequest.SerializeToString,
            bragi_dot_bragi__pb2.CsgoScoreBoard.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CsgoEventsFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bragi.BragiGrpc/CsgoEventsFeed',
            bragi_dot_bragi__pb2.CsgoEventsFeedRequest.SerializeToString,
            bragi_dot_bragi__pb2.CsgoEvents.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
