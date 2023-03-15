from django import forms
from . models import *
from django.utils.translation import gettext as _
from django_summernote.widgets import SummernoteWidget

class ProductForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'old_price', 'description', 'body', 'language']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'language': forms.Select(attrs={'class': 'form-select'}),
        }




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }



class BenefitForm(forms.ModelForm):
    class Meta:
        model = Benefit
        fields = ['title', 'description', 'language']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
            'language': forms.Select(attrs={'class': 'form-select'}),
        }



class PostForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ['title', 'image', 'description', 'body', 'language']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-select'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'payment']