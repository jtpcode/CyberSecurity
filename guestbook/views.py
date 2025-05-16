from django.shortcuts import render, redirect
from .models import Message

from django.utils.safestring import mark_safe

# Create your views here.


def index(request):
    # 2.   Broken access control -vulnerability:
    messages = Message.objects.order_by("-created_at")
    # FIX for Broken access control: replace the above line with the line below,
    # so messages are filtered according to privacy
    # messages = Message.objects.filter(is_public=True).order_by("-created_at")

    # 1. Cross Site Script (XSS) -vulnerability:
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
        is_public = not request.POST.get("is_private")

        Message.objects.create(
            name=name, email=email, content=content, is_public=is_public)

        return redirect("index")
    return render(request, "guestbook/submit.html")
