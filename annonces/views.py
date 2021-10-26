from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import AnnoncesForm
from .models import Annonce


# Create your views here.
class AnnonceListeView(ListView):
    model = Annonce
    context_object_name = "annonces"
    template_name = "annonces/annonce_liste.html"


class AnnonceDetailView(DetailView):
    model = Annonce
    context_object_name = "annonce"
    template_name = "annonces/annonce_detail.html"


class AnnonceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Annonce
    form_class = AnnoncesForm
    context_object_name = "form"
    success_url = reverse_lazy("annonce-list")
    success_message = "Votre annonce a été crée !"
    template_name = "annonces/annonce_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnnonceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Annonce
    form_class = AnnoncesForm
    context_object_name = "form"
    success_url = "/annonces/my-annonces/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        annonce = self.get_object()
        if self.request.user == annonce.author:
            return True
        return False


class AnnonceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Annonce
    template_name = "annonces/annonce_confirm_delete.html"
    success_url = "/annonces/my-annonces/"

    def test_func(self):
        annonce = self.get_object()
        if self.request.user == annonce.author:
            return True
        return False


@login_required
def annonces_user(request):
    annonces = Annonce.objects.filter(author=request.user)
    context = {"annonces": annonces}
    return render(request, "annonces/annonce_user.html", context)


