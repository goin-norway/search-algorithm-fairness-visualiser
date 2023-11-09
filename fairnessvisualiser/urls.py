from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fairness-visualiser", views.fairness_visualiser, name="fairness-visualiser"),
]