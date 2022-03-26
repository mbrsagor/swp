from rest_framework import serializers
from user.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            'id', 'mentor', 'submission', 'grades', 'created_at'
        )
