from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }
                                                    ))
    password = forms.CharField(widget=forms.PasswordInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }
                                                    ))