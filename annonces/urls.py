from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.AnnonceCreateView.as_view(), name="annonce-create"),
    path('list/', views.AnnonceListeView.as_view(), name="annonce-list"),
    path('list/<str:pk>/', views.AnnonceDetailView.as_view(), name="annonce-detail"),
    path('list/<str:pk>/update/', views.AnnonceUpdateView.as_view(), name="annonce-update"),
    path('list/<str:pk>/delete/', views.AnnonceDeleteView.as_view(), name="annonce-delete"),
    path('my-annonces/', views.annonces_user, name="annonce-user"),
]