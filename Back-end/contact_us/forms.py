from django import forms

from .models import Contact, Subscribers

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'

         
        error_messages = {
            "email":{
                "required":"email cannot be blank!",
                "max_length": "please enter a shorter email"
            },
            "message":{
                "required":"message cannot be blank!",
                "max_length": "please enter a shorter email"
            }
        }
 

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers  
        fields= '__all__'
          
        error_messages = {
            "subscribers_email":{
                "required":"email cannot be blank!",
                "max_length": "please enter a shorter email"
            }
            }