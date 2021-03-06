from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


# Create your models here.
class Condition(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Condition, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

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

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
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


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    subcategory = models.ForeignKey(SubCategory, related_name="items",
                                    on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.PositiveIntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name="items")
    tag = models.ManyToManyField(Tag, related_name="items", blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="items", blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="items", blank=True, default=Size.ordering)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    give = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


