from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_message, name="submit_message"),
    path("logout/", views.logout_view, name="logout"),
]
