from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                               min_length=4, max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'placeholder': 'digite el nombre de usuario'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'id': 'email',
                                 'placeholder': 'ejemplo@gmail.com'
                             }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs)
                               'class': )
