from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1",]
