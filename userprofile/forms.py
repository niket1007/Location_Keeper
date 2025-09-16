from django import forms

class PasswordUpdateForm(forms.Form):
    password = forms.CharField(
        min_length=3,
        max_length=15,
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'title': 'Enter your password',
                'placeholder': 'Enter your password'})
    )

    confirm_password = forms.CharField(
        min_length=3,
        max_length=15,
        required=True,
        label="Confirm Password",
        widget=forms.TextInput(
            attrs={
                'title': 'Enter your confirm password',
                'placeholder': 'Enter your confirm password'})
    )

    def clean_password(self):
        value = self.cleaned_data['password']
        if value == "" or value is None:
            raise forms.ValidationError('Password cannot be empty')
        return value
    
    def clean_confirm_password(self):
        value = self.cleaned_data['confirm_password']
        if value == "" or value is None:
            raise forms.ValidationError('Confirm password cannot be empty')
        return value
    
    def clean(self):
        values = self.cleaned_data
        if values.get("password", None) != values.get("confirm_password", None):
            self.add_error(None, 'Password and confirm password should be equal.')

class NameUdpateForm(forms.Form):
    full_name = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'title': 'Enter your name',
                'placeholder': 'Enter your name'})
    )

    username = forms.CharField(
        min_length=5,
        max_length=15,
        required=True,
        label="Username",
        widget=forms.TextInput(
            attrs={
                'disabled': 'true',
                'title': 'Enter your username',
                'placeholder': 'Enter your username'})
    )

    def clean_full_name(self):
        value = self.cleaned_data['full_name']
        if value == "" or value is None:
            raise forms.ValidationError('Name cannot be empty')
        return value