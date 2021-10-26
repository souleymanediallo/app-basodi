from django import forms
from .models import Annonce, Category


class AnnoncesForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ["category", "name", "description", "price", "size", "color", "tag", "condition", "give", "photo_main"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields["category"].queryset = Category.objects.filter(parent__isnull=True)
        # self.fields["souscategory"].queryset = Category.objects.filter(parent__variants__category="souscategory")
        # self.fields["souscategory"].queryset = Category.objects.filter(parent__isnull=False)
