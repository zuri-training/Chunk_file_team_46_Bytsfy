from django.shortcuts import render


from django.views.generic.edit import CreateView


from .models import Contact,Subscribers
from .forms import ContactForm,SubscribersForm
# Create your views here.

class ContactView(CreateView):
    model = Contact
    template_name = "contact_us/contact.html"
    form_class = ContactForm
    success_url ="/"


class SubscriberView(CreateView):
    model = Subscribers
    template_name = "contact_us/includes/subscription.html"
    form_class = SubscribersForm
    success_url ="/"
