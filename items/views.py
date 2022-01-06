from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Item
from .forms import ItemForm
# Create your views here.


class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    context_object_name = "form"
    success_url = reverse_lazy("annonce-list")
    success_message = "Votre annonce a été crée !"
    template_name = "items/item_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)