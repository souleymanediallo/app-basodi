from django.contrib import admin
from .models import Annonce, Category, Tag, Color, Size
# Register your models here.


class AnnonceAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class SizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)