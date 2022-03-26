from rest_framework import views, status
from rest_framework.response import Response

from user.models import Assessment
from user.serializers.assessment_serializer import AssessmentSerializer
from user.utils import ROLE


class AssessmentCreateListView(views.APIView):

    def post(self, request):
        role_perm = request.user.role
        try:
            if role_perm == ROLE.ADMIN or role_perm == ROLE.MENTOR:
                serializer = AssessmentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(mentor=request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('You have no permission to create assessment.', status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e))

    def get(self, request):
        role_perm = request.user.role
        try:
            if role_perm == ROLE.ADMIN or role_perm == ROLE.MENTOR:
                assessment = Assessment.objects.filter(mentor=request.user)
                serializer = AssessmentSerializer(assessment, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('You have no permission.', status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response(str(e))
