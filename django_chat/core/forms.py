from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        # use default user model
        model = User
        # pick fields to use
        fields = ['username', 'password1', 'password2']

