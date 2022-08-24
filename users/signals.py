from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User, Student, Teacher, StudentProfile, TeacherProfile, AdminProfile

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(user=instance)


@receiver(pre_save, sender=StudentProfile)
def uniqie_id_genarate(sender, instance, **kwargs):
    if instance.roll_number:
        year_last_two_digit = instance.created_at.strftime("%y")
        instance.unique_id = f'075{year_last_two_digit}100{instance.program.code}{instance.roll_number}'

