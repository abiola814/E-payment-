# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class CustomUSerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1',]


    def __init__(self, *args, **kwargs):
        super(CustomUSerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-50 mb-3 form-control'})

        # w-50 mb-3 form-control

