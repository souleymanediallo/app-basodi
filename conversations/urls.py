from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("conversation/<str:pk>/", views.conversation_list, name="conversation"),
    path("conversation-create/<str:pk>/", views.conversation_create, name="conversation-create"),

]
