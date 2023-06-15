from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import PictureDb
from .forms import PictureDbForm


def home(request):
    return HttpResponse("Welcome to my webpage!")


def picturedb_list(request):
    picturedbs = PictureDb.objects.all()
    return render(request, 'picturedb_list.html', {'picturedbs': picturedbs})


def add_picturedb(request):
    if request.method == 'POST':
        form = PictureDbForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('picturedb_list')
    else:
        form = PictureDbForm()

    return render(request, 'add_picturedb.html', {'form': form})


def delete_picturedb(request, pk):
    picturedb = get_object_or_404(PictureDb, pk=pk)
    if request.method == 'POST':
        picturedb.delete()
        return redirect('picturedb_list')
    return render(request, 'picturedb_delete.html', {'picturedb': picturedb})

