from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    crud = CRUD.objects.all()
    return render(request, 'home.html', locals())


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        cat = request.POST['cat']
        email = request.POST['email']
        image = request.FILES['image']
        crud = CRUD(name=name, cat=cat, email=email, image=image)
        crud.save()
        return redirect('home')
    else:
        return render(request, 'create.html')


def update(request, id):
    crud = CRUD.objects.filter(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        cat = request.POST['cat']
        email = request.POST['email']
        image = request.FILES['image']
        crud = CRUD(id=id, name=name, cat=cat, email=email, image=image)
        crud.save()
        return redirect('home')

    return render(request, 'update.html', locals())


def delete(request, id):
    crud = CRUD.objects.get(id=id)
    crud.delete()
    return redirect('home')
