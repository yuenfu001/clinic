from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("contact/", views.Add, name="contact"),
    path("edit/<str:edit>/", views.Edit, name="edit"),
    path("delete_contact/<str:delete>/", views.Delete, name="delete"),
    path("view-contact/<str:view>/", views.ViewDetail, name="view"),
]
