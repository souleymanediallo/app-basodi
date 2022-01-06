from django.contrib import admin
from .models import Color, Category, Condition, SubCategory, Size, Item
# Register your models here.

admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(SubCategory)
admin.site.register(Size)
admin.site.register(Item)