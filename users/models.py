from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from users.managers import UserManager
from portal.models.domain_entity import DomainEntity

# Custom user created.
class User(AbstractBaseUser, PermissionsMixin):

    #TODO:full_name change 

    class Rolls(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'

    full_name = models.CharField(max_length=155, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    roll = models.CharField(choices=Rolls.choices, default=Rolls.STUDENT, max_length=7, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    # def get_absolute_url(self):
    #     return reverse('accounts:dashboard_view', kwargs={'pk': self.pk})




class Profile(DomainEntity):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userProfile')
    name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    board_roll = models.CharField(max_length=100, blank=True, null=True)
    ssc_passing_year = models.DateField(blank=True, null=True)
    hsc_passing_year = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)

    def __str__(self):
        return self.user.email



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(user=instance)
        return profile


post_save.connect(create_user_profile, sender=User)