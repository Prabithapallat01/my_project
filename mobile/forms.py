from django import forms
from django.forms import ModelForm
from .models import Brands
from .models import Mobile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Orders

class BrandCreationForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'



class BrandUpdateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'
        widgets={
            'brand_name': forms.TextInput(attrs={'class': 'brand_name'}),

        }

class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']



class OrderedProduct(ModelForm):
    class Meta:
        model=Orders
        fields='__all__'