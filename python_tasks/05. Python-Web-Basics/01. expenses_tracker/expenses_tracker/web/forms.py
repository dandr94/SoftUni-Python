import os

from django import forms

from expenses_tracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'image']


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fields in self.fields.items():
            fields.widget.attrs['disabled'] = 'disabled'
            fields.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'image']


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = []
