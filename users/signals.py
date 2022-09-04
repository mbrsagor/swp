from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, AdminProfile


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(user=instance)
