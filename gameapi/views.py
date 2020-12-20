from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import filters

from .models import Frames
from .serializers import FrameSerializers
from .calculation import calculate_total_score


# Create your views here.


class FrameViewSet(ViewSet):
    """ViewSet class for game to start, continue and track """
    queryset = Frames.objects.all()
    serializer_class = FrameSerializers


    def get_object(self, pk):
        """Get each object bt id"""
        data = get_object_or_404(self.queryset, pk=pk)
        return data

    def retrieve(self, request, pk=None):
        """Retrieve each data by id(get)"""
        data = self.get_object(pk)
        serializer_data = self.serializer_class(data)
        return Response(serializer_data.data)

    def list(self, request):
        """To show list of all game played(list)"""
        serializer_data = self.serializer_class(self.queryset, many=True)
        return Response(serializer_data.data)

    def create(self, request):
        """To create each game with unique player name(post)"""
        serializers_data = self.serializer_class(data=request.data)
        if serializers_data.is_valid():
            frame1_1 = serializers_data.validated_data['frame1_first']
            frame1_2 = serializers_data.validated_data['frame1_second']
            frame2_1 = serializers_data.validated_data['frame2_first']
            frame2_2 = serializers_data.validated_data['frame2_second']
            frame3_1 = serializers_data.validated_data['frame3_first']
            frame3_2 = serializers_data.validated_data['frame3_second']
            frame4_1 = serializers_data.validated_data['frame4_first']
            frame4_2 = serializers_data.validated_data['frame4_second']
            frame5_1 = serializers_data.validated_data['frame5_first']
            frame5_2 = serializers_data.validated_data['frame5_second']
            frame6_1 = serializers_data.validated_data['frame6_first']
            frame6_2 = serializers_data.validated_data['frame6_second']
            frame7_1 = serializers_data.validated_data['frame7_first']
            frame7_2 = serializers_data.validated_data['frame7_second']
            frame8_1 = serializers_data.validated_data['frame8_first']
            frame8_2 = serializers_data.validated_data['frame8_second']
            frame9_1 = serializers_data.validated_data['frame9_first']
            frame9_2 = serializers_data.validated_data['frame9_second']
            frame10_1 = serializers_data.validated_data['frame10_first']
            frame10_2 = serializers_data.validated_data['frame10_second']
            frame10_bonus = serializers_data.validated_data['frame10_bonus']

            frame_list = [[frame1_1, frame1_2], [frame2_1, frame2_2],
                          [frame3_1, frame3_2], [frame4_1, frame4_2],
                          [frame5_1, frame5_2], [frame6_1, frame6_2], [frame7_1, frame7_2], [frame8_1, frame8_2],
                          [frame9_1, frame9_2], [frame10_1, frame10_2, frame10_bonus]]

            total_score = calculate_total_score(frame_list)[0]
            frame_score = calculate_total_score(frame_list)[1]

            serializers_data.save(total_score=total_score, all_frame_score=frame_score)
            return Response(serializers_data.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Get each item to updated and game continue, need to click save button every after ball score update(put)"""

        frame_data = self.get_object(pk)
        serializers_data = self.serializer_class(frame_data, data=request.data, partial=True)
        if serializers_data.is_valid():
            frame1_1 = serializers_data.validated_data['frame1_first']
            frame1_2 = serializers_data.validated_data['frame1_second']
            frame2_1 = serializers_data.validated_data['frame2_first']
            frame2_2 = serializers_data.validated_data['frame2_second']
            frame3_1 = serializers_data.validated_data['frame3_first']
            frame3_2 = serializers_data.validated_data['frame3_second']
            frame4_1 = serializers_data.validated_data['frame4_first']
            frame4_2 = serializers_data.validated_data['frame4_second']
            frame5_1 = serializers_data.validated_data['frame5_first']
            frame5_2 = serializers_data.validated_data['frame5_second']
            frame6_1 = serializers_data.validated_data['frame6_first']
            frame6_2 = serializers_data.validated_data['frame6_second']
            frame7_1 = serializers_data.validated_data['frame7_first']
            frame7_2 = serializers_data.validated_data['frame7_second']
            frame8_1 = serializers_data.validated_data['frame8_first']
            frame8_2 = serializers_data.validated_data['frame8_second']
            frame9_1 = serializers_data.validated_data['frame9_first']
            frame9_2 = serializers_data.validated_data['frame9_second']
            frame10_1 = serializers_data.validated_data['frame10_first']
            frame10_2 = serializers_data.validated_data['frame10_second']
            frame10_bonus = serializers_data.validated_data['frame10_bonus']

            frame_list = [[frame1_1, frame1_2], [frame2_1, frame2_2],
                          [frame3_1, frame3_2], [frame4_1, frame4_2],
                          [frame5_1, frame5_2], [frame6_1, frame6_2], [frame7_1, frame7_2], [frame8_1, frame8_2],
                          [frame9_1, frame9_2], [frame10_1, frame10_2, frame10_bonus]]

            total_score = calculate_total_score(frame_list)[0]
            frame_score = calculate_total_score(frame_list)[1]

            serializers_data.save(total_score=total_score, all_frame_score=frame_score)
            return Response(serializers_data.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)
