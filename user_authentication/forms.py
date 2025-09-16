from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=15,
        required=False,
        label='Username',
        widget=forms.TextInput(
            attrs={
                'title': 'Enter your username',
                'placeholder': 'Enter your username'})
    )
    
    password = forms.CharField(
        min_length=3,
        max_length=15,
        required=False,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'title': 'Enter your password',
                'placeholder': 'Enter your password'})
    )

    def clean_username(self):
        value = self.cleaned_data['username']
        if value == "" or value is None:
            raise forms.ValidationError('Username cannot be empty')
        return value
    
    def clean_password(self):
        value = self.cleaned_data['password']
        if value == "" or value is None:
            raise forms.ValidationError('Password cannot be empty')
        return value

class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=15,
        required=False,
        label="Username",
        widget=forms.TextInput(
            attrs={
                'title': 'Enter your username',
                'placeholder': 'Enter your username'})
    )
    
    password = forms.CharField(
        min_length=3,
        max_length=15,
        required=False,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'title': 'Enter your password',
                'placeholder': 'Enter your password'})
    )

    full_name = forms.CharField(
        required=False,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'title': 'Enter your name',
                'placeholder': 'Enter your name'})
    )

    def clean_full_name(self):
        value = self.cleaned_data['full_name']
        if value == "" or value is None:
            raise forms.ValidationError('Name cannot be empty')
        return value

    def clean_username(self):
        value = self.cleaned_data['username']
        if value == "" or value is None:
            raise forms.ValidationError('Username cannot be empty')
        return value
    
    def clean_password(self):
        value = self.cleaned_data['password']
        if value == "" or value is None:
            raise forms.ValidationError('Password cannot be empty')
        return value