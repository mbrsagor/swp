from rest_framework import views, status
from rest_framework.response import Response

from user.models import Submission
from user.serializers.submission_serializer import SubmissionSerializer


class SubmissionAPIView(views.APIView):

    def post(self, request):
        try:
            serializer = SubmissionSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(str(ex))

    def get(self, request):
        submission = Submission.objects.filter(user=request.user)
        if submission is not None:
            serializer = SubmissionSerializer(submission, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No data found', status=status.HTTP_204_NO_CONTENT)
