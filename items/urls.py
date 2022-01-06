from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name="item-list"),
    path('new', views.ItemCreateView.as_view(), name="item-new"),
]