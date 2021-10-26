from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.AnnonceCreateView.as_view(), name="annonce-create"),
    path('list/', views.AnnonceListeView.as_view(), name="annonce-list"),
    path('list/<str:pk>/', views.AnnonceDetailView.as_view(), name="annonce-detail"),
    #path('list/user/', views.AnnonceUserView.as_view(), name="annonce-user"),
    path('my-annonces/', views.annonces_user, name="annonce-user"),
]