from django.shortcuts import render

#! Product View
def index(request):
    return render(request,"index.html")

def list_products(request):
    return render(request,"products.html")

def detail_product(request):
    return render(request,"product_detail.html")