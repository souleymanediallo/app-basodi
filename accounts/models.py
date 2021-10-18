from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from .choices import CITY_CHOICES

# CustomUser
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None,):

        if not email:
            raise ValueError("L'email est obligatoire")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_active = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["email"]

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default="user.png", upload_to="photos", blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(blank=True, null=True, choices=CITY_CHOICES, default="Dakar")
    description = models.TextField(max_length=300, blank=True, null=True)
    instagram = models.URLField(max_length=400, blank=True, null=True)
    facebook = models.URLField(max_length=400, blank=True, null=True)
    youtube = models.URLField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ProfilePersonnel(Profile):
    is_active = models.BooleanField(default=True)


class ProfileProfessional(Profile):
    is_active = models.BooleanField(default=True)
    website = models.URLField(max_length=400, blank=True, null=True)


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        if instance.status == "PARTICULIER":
            ProfilePersonnel.objects.create(user=instance)
        else:
            ProfileProfessional.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)
