from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, Student, Teacher, StudentProfile, TeacherProfile


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=Teacher)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)

