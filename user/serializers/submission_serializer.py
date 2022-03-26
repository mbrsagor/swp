from rest_framework import serializers
from user.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        read_only_fields = ('user',)
        fields = (
            'id', 'user', 'submission_user', 'assessment', 'assessment_name', 'link',
            'file', 'created_at', 'updated_at'
        )
