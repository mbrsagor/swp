import django_filters
from django_filters import filters
from faculties.models import Assignment, CourseSchedule


def course_schedule(request):
    if request.user.teacher:
        return CourseSchedule.objects.filter(teacher=request.user)
    return CourseSchedule.objects.all()


class AssignmentFilter(django_filters.FilterSet):
    course_schedule = filters.ModelChoiceFilter(queryset=course_schedule)

    class Meta:
        model = Assignment
        fields = ['course_schedule']
