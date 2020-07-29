from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


# class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = User

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Email address"

class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        fields = ("username", "email")
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
