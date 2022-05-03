from django.shortcuts import render, redirect

from notes.web.forms import CreateProfileForm, AddNoteForm, DeleteNoteForm, EditNoteForm, ShowDetailsForm
from notes.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()

    if profile:
        return profile[0]

    return None


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
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


def show_index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    total_notes = len(notes)

    context = {
        'profile': profile,
        'notes': notes,
        'total_notes': total_notes
    }

    return render(request, 'profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = AddNoteForm()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = ShowDetailsForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = ShowDetailsForm(instance=note)

    context = {
        'form': form,
        'note': note
    }

    return render(request, 'note-details.html', context)
