from rest_framework import serializers
from user.models import Assessment


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        read_only_fields = ('mentor',)
        fields = (
            'mentor', 'mentor_name', 'title', 'description', 'date_line', 'created_at'
        )
