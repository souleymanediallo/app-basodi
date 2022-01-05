from django.shortcuts import render
from annonces.models import Annonce
from django.views.generic import ListView, TemplateView
from annonces.models import Annonce


# Create your views here.
class HomeView(ListView):
    model = Annonce
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["annonces"] = Annonce.objects.all()
        return context

# def home(request):
#     annonces = Annonce.objects.all()
#     context = {annonces: annonces}
#     return render(request, "pages/index.html", context)