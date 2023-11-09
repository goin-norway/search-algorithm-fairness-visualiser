from django.shortcuts import render
from fairnessvisualiser.helloworld import hello_world

def home(request):
    return render(request, "templates/home.html")

def fairness_visualiser(request):
    return render(request, "templates/fairness-visualiser.html", { "metric": round(hello_world() * 100, 2) })