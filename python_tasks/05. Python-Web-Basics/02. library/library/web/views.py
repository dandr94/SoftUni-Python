from django.shortcuts import render, redirect

from library.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, AddBookForm, DetailsBookForm, \
    EditBookForm

from library.web.models import Profile, Book


def give_profile():
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
        'no_profile': True
    }

    return render(request, 'home-no-profile.html', context)


def show_index(request):
    profile = give_profile()

    if not profile:
        return redirect('create profile')

    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = give_profile()

    content = {
        'profile': profile
    }

    return render(request, 'profile.html', content)


def edit_profile(request):
    profile = give_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = give_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'delete-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = AddBookForm()

    context = {
        'form': form
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show index')

    else:
        form = EditBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
    }

    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }

    return render(request, 'book-details.html', context)



def delete_book(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('show index')

