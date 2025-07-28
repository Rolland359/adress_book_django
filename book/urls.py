from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    # home page
    path("", views.index, name="index"),
    # generate formular to create a new contact
    path("create/", views.create, name="create"),
    # contact details
    path("<int:contact_id>/contacts/", views.details, name="details"),
    # process the creation of a new contact
    path("add/", views.process_create, name="process_create"),
    # generate formular to update a contact
    path("<int:contact_id>/update/", views.update, name="update"),
    # process the update of a contact
    path("<int:contact_id>/process_update/", views.process_update, name="process_update"),
    # process the deletion
    path("<int:contact_id>/process_delete/", views.process_delete, name="process_delete"),
]
