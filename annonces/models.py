from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
from .choices import CONDITION_CHOICES
import uuid


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Annonce(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="annonces")
    souscategory = models.ForeignKey(Category, related_name="variants", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)
    tag = models.ManyToManyField(Tag, related_name="annonces", blank=True)
    color = models.ManyToManyField(Color, related_name="annonces", blank=True)
    size = models.ManyToManyField(Size, related_name="annonces", blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    give = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Annonce, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("annonce-detail", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("annonce-delete", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("annonce-update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


