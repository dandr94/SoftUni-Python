from django import forms

from library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'type']


class DetailsBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'type']


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'type']