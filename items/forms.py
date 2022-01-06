from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        TITLE_CHOICES = "TITLE_CHOICES"
        model = Item
        fields = ["category", "subcategory", "name", "description", "price", "condition", "tag", "color", "size",
                  "photo_main", "photo_1", "photo_2", "photo_3", "photo_4", "photo_5", "photo_6"]

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            self.fields['size'].widget.attrs.update({'placeholder': 'Pas de Taille'})
            self.fields['photo_main'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_1'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_2'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_3'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_4'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_5'].widget.attrs.update({'class': 'custom-file-upload'})
            self.fields['photo_6'].widget.attrs.update({'class': 'custom-file-upload'})


# https://www.w3schools.com/bootstrap4/bootstrap_forms_custom.asp

# <form>
# <div class="custom-file">
# <input type="file" class="custom-file-input" id="customFile">
# <label class="custom-file-label" for="customFile">Choose file</label>
# </div>
# </form>
#
# <script>
# // Add the following code if you want the name of the file appear on select
# $(".custom-file-input").on("change", function() {
#     var fileName = $(this).val().split("\\").pop();
# $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
# });
# </script>
