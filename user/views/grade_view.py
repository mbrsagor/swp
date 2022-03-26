from rest_framework import views, status
from rest_framework.response import Response

from user.models import Grade
from user.serializers.grade_serializer import GradeSerializer
from user.utils import ROLE


class GradeAPIView(views.APIView):

    def post(self, request):
        role_perm = request.user.role
        try:
            if role_perm == ROLE.ADMIN or role_perm == ROLE.MENTOR:
                serializer = GradeSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(mentor=self.request.user)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response('You have no permission', status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            return Response(str(ex))

    def get(self, request):
        role_perm = request.user.role
        if role_perm == ROLE.ADMIN or role_perm == ROLE.MENTOR:
            grade = Grade.objects.filter(mentor=self.request.user)
            if grade is not None:
                serializer = GradeSerializer(grade, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('No content found', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('You have no permission', status=status.HTTP_401_UNAUTHORIZED)


class GradeDetailView(views.APIView):

    def get(self, request, pk):
        role_perm = request.user.role
        if role_perm == ROLE.ADMIN or role_perm == ROLE.MENTOR:
            grade = Grade.objects.get(id=pk)
            if grade is not None:
                serializer = GradeSerializer(grade)
                return Response(serializer.data)
            return Response('No content found')
        else:
            return Response('You have no permission', status=status.HTTP_401_UNAUTHORIZED)
