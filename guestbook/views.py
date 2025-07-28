import subprocess
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.safestring import mark_safe
from .models import Message

# Create your views here.


@login_required
def index(request):
    # FLAW 2: Broken access control -vulnerability.
    messages = Message.objects.order_by("-created_at")
    # FIX for Broken access control: replace the above line with the line below,
    # so messages are filtered according to privacy.
    # messages = Message.objects.filter(is_public=True).order_by("-created_at")

    # FLAW 1: Cross Site Script (XSS) -vulnerability.
    for msg in messages:
        msg.content = mark_safe(msg.content)
    # FIX for XSS: remove the for-loop completely, so messages aren't marked
    # as safe.

    return render(request, "guestbook/index.html", {"messages": messages})


# FLAW 4: CSRF -vulnerability.
@csrf_exempt
# FIX for CSRF -vulnerability: remove the "@csrf_exempt" AND ALSO
# add "{% csrf_token %}" in "submit.html" form.

@login_required
def submit_message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("content")
        is_public = not request.POST.get("is_private")

        Message.objects.create(
            name=name, email=email, content=content, is_public=is_public
        )

        # FLAW 5: Injection -vulnerability.
        subprocess.call(f"echo {name}", shell=True)
        # FIX for Injection -vulnerability: remove subprocess.call from the code
        # and preferrably use print for debugging inputs:
        # print("User input from:", name)

        return redirect("index")
    return render(request, "guestbook/submit.html")


def logout_view(request):
    logout(request)

    return redirect("index")
