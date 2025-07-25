from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
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

def process_add(request):
    print("utiliseateur sauvegardé")

def process_delete(request, contact_id):
    pass
