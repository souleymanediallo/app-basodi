from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
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


@login_required
def annonces_user(request):
    annonces = Annonce.objects.filter(author=request.user)
    context = {"annonces": annonces}
    return render(request, "annonces/annonce_user.html", context)


