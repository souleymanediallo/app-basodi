from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from .choices import CITY_CHOICES
from django.urls import reverse
import uuid


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
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

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
    location = models.CharField(blank=True, null=True, choices=CITY_CHOICES, max_length=100, default="Dakar")
    description = models.TextField(max_length=300, blank=True, null=True)
    instagram = models.URLField(max_length=400, blank=True, null=True)
    facebook = models.URLField(max_length=400, blank=True, null=True)
    youtube = models.URLField(max_length=400, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)
