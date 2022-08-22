from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User, Student, Teacher, StudentProfile, TeacherProfile, AdminProfile

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(user=instance)

@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=Teacher)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)

@receiver(pre_save, sender=StudentProfile)
def uniqie_id_genarate(sender, instance, **kwargs):
    if instance.roll_number:
        year_last_two_digit = instance.created_at.strftime("%y")
        print(year_last_two_digit)
        instance.unique_id = f'521{instance.faculty.code}{year_last_two_digit}{instance.program.code}{instance.roll_number}'

