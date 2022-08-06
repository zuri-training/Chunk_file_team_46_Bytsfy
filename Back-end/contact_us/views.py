from django.shortcuts import render


from django.views.generic.edit import CreateView


from .models import Contact
from .forms import ContactForm
# Create your views here.

class ContactView(CreateView):
    model = Contact
    template_name = "contact_us/contact.html"
    form_class = ContactForm
    success_url ="/"
