from django.http import HttpResponse
from django.shortcuts import render

from contact.forms import ContactMessageModelForm


def contact_page(request):
    if request.method == "POST":
        form = ContactMessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Richiesta presa in carico!</h1>")
    else:
        form = ContactMessageModelForm()
    context = {"form": form}
    return render(request, "contact/contact_page.html", context)
