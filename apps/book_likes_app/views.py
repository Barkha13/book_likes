from django.shortcuts import render, HttpResponse, render

# Create your views here.
def index(request):
    response = "This is book/likes app"
    return HttpResponse(response)