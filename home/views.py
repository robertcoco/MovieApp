from django.shortcuts import render

#home view testing

def home(request):
    return render(request, "home/main.html")
