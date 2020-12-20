from rest_framework import serializers
from .models import Frames


class FrameSerializers(serializers.ModelSerializer):
    """Serializers for Frame Model"""

    class Meta:
        model = Frames
        fields = '__all__'
        read_only_fields = ('total_score', 'all_frame_score',)
