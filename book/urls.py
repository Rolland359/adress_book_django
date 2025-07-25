from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:contact_id>/contacts/", views.details, name="details"),
    path("create/", views.create, name="create"),
    path("add/", views.process_add, name="process_add"),
    path("<int:contact_id>/update/", views.update, name="update"),
    path("<int:contact_id>", views.process_delete, name="process_delete"),
]
