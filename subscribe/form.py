from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

        labels = {
            'fname':_('Enter First Name'),
            'lname':_('Enter Last Name'),
            'email':_('Enter Email'),
            'option':_('Select Type'),
        }
        error_messages = {
            'fname':{
                'required':_('fname')
                },
            'lname':{
                'required':_('lname')
                },
            'email':{
                'required':_('email')
                },
        }