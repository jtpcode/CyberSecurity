from django.shortcuts import render, redirect
from .models import Message

from django.utils.safestring import mark_safe

# Create your views here.


def index(request):
    messages = Message.objects.filter(is_public=True).order_by("-created_at")
    for msg in messages:
        msg.content = mark_safe(msg.content)
    # FIX for XSS: remove the for-loop completely, so messages aren't marked
    # as safe.

    return render(request, "guestbook/index.html", {"messages": messages})


def submit_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")
        Message.objects.create(name=name, email=email, content=content)

        return redirect("index")
    return render(request, "guestbook/submit.html")
