from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name',"card_ID","sex","age","tel","address")
    form = ContactCreateForm

admin.site.register(Contact,ContactAdmin)
