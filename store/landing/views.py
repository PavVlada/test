from django.shortcuts import render
from .forms import UserForm
from products.models import *


def landing(request):
    form = UserForm(request.POST or None)
    if request.POST and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())