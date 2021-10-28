from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("conversation/<str:conversation_id>/", views.conversation_list, name="conversation"),
    path("conversation-create/<int:conversation_id>/", views.conversation_create, name="conversation-create"),

]
