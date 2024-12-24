from django.shortcuts import render

#! Product View
def index(request):
    return render(request,"index.html")