from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from healthapp.forms import ProductForm
from healthapp.models import Sale, Product


# Create your views here.

def index(request):
    sales = Sale.objects.all()
    return render(request, 'index.html', context={'sales':sales})

def outofstock(request):
    products = Product.objects.filter(quantity=0, category__is_active=True)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()

        return redirect('index')

    form = ProductForm()
    return render(request, 'outofstock.html', context={'form': form, 'products': products})