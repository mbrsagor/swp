from rest_framework import serializers
from user.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        read_only_fields = ('mentor',)
        fields = (
            'id', 'mentor', 'submission', 'grade', 'created_at'
        )
