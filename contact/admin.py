from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',"patient_id","age","phone_number","address")
    form = ContactCreateForm

admin.site.register(Contact,ContactAdmin)
