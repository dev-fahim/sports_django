from django import forms

from user_profile.models import GenderChoice


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField()

    gender = forms.ChoiceField(choices=GenderChoice.choices, required=True)
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=11, required=True)

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_confirm']:
            self._errors["password"] = ["Password do not match"]
            del form_data['password']
        return form_data
