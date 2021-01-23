from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        'shows': TV_Show.objects.all()
    }
    return render(request, 'shows.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    print(request.POST)
    errors = TV_Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = TV_Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release'],
            description=request.POST['description']
        )
        return redirect(f'/shows/{show.id}')


def view_show(request, show_id):
    context = {
        'view_show': TV_Show.objects.get(id=show_id)
    }
    return render(request, 'view_show.html', context)


def delete_show(request, show_id):
    delete_this_show = TV_Show.objects.get(id=show_id)
    delete_this_show.delete()
    return redirect('/shows')


def edit_show(request, show_id):
    context = {
        'edit_show': TV_Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)


def update(request, show_id):
    print(request.POST)
    errors = TV_Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = TV_Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
