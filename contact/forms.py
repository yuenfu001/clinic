from django import forms
from .models import *

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name",'patient_id','age','phone_number','address',]