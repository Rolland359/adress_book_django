from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Contact
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    contacts = get_list_or_404(Contact)
    context = {'contact_list': contacts}
    return render(request, "book/index.html", context)

def details(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {"contact":contact}
    return render(request, "book/details.html", context)

def create(request):
    return render(request, "book/create.html")

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {"contact":contact}
    return render(request, "book/update.html", context)

def general_process(request):
    type_daction = request.POST.get("action")
    if type_daction == "add":

        new_contact = Contact()

        new_contact.name = request.POST.get("name")
        new_contact.lastname = request.POST.get("lastname")
        new_contact.phone = request.POST.get("phone")
        new_contact.email = request.POST.get("email")
        new_contact.email = request.POST.get("email")
        new_contact.address = request.POST.get("email")
        new_contact.photo = request.POST.get("photo")
        new_contact.save()

        return HttpResponseRedirect(reverse("book:index", args=()))
    
    elif type_daction == "update":
        return HttpResponseRedirect(reverse("book:index", args=()))

def process_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {"contact":contact, "message":"delete"}
    return render(request, "book/update.html", context)
