from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
#	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def sign_up(request):
	return render(request, 'sign_up.html', {})

def add_products(request):
    return render(request, 'add_products.html', {})

def details_products(request):
    return render(request, 'details_products.html', {})

def pedido(request):
    return render(request, 'pedido.html', {})