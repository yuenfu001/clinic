from contact.forms import ContactCreateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def Home(request):
    contact = Contact.objects.all()
    form = SearchContactForm(request.POST or None)
    context = {
        "contact": contact,
        "search":form
    }
    if request.method=="POST":
        contact = Contact.objects.filter(tel__icontains=form["tel"].value())

    return render(request, "base/index.html", context)


def Add(request):
    form = ContactCreateForm(request.POST or None)
    context = {
        "add": form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "other/add.html", context)


def Edit(request, edit):
    edit = get_object_or_404(Contact, id=edit)
    form = ContactEditForm(instance=edit)
    context = {
        "edit": edit,
        "edit_form": form,
    }
    if request.method == "POST":
        form = ContactEditForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "other/edit.html", context)


def Delete(request, delete):
    delete = get_object_or_404(Contact, id=delete)
    context = {
        "delete": delete,
    }
    if request.method == "POST":
        delete.delete()
        return redirect("home")

    return render(request, "other/delete.html", context)

def ViewDetail(request, view):
    view_detail = Contact.objects.filter(id=view)
    context = {
        "view":view_detail,
    }
    return render(request, "other/view.html", context)