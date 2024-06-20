from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://fakestoreapi.com/products')
    item=response.json()
    context = {
        "item":item
    }
    return render(request,"index.html",context)

