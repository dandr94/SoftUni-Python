from django.shortcuts import render, redirect

from my_music_app.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()

    if profile:
        return profile[0]

    return None


def show_index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = AddAlbumForm()

    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()
    albums_count = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums_count': albums_count
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile
    }

    return render(request, 'profile-delete.html', context)
