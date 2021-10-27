from django.shortcuts import render, redirect
from .forms import ConversationForm
from accounts.models import Profile
from .models import Conversation
from django.contrib import messages


# Create your views here.
def inbox(request):
    profile = request.user
    conversation_requests = profile.conversations.all()
    unread_count = conversation_requests.filter(is_read=False).count()
    context = {"conversation_requests": conversation_requests, "unread_count": unread_count}
    return render(request, "conversations/inbox.html", context)


def conversation_list(request, pk):
    profile = request.user
    conversation = profile.conversations.get(id=pk)
    if conversation.is_read == False:
        conversation.is_read = True
        conversation.save()
    context = {"conversation": conversation}
    return render(request, "conversations/conversation.html", context)


def conversation_create(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = ConversationForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = ConversationForm(request.POST)
        if form.is_valid():
            conversation = form.save(commit=False)
            conversation.sender = sender
            conversation.recipient = recipient

            if sender:
                conversation.name = sender.name
                conversation.email = sender.email
            conversation.save()

            messages.success(request, "Votre message été envoyé !")
            return redirect("home")

        context = {"recipient": recipient, "form": form}
        return render(request, "conversations/conversation_form.html", context)
