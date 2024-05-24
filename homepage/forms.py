from django import forms
from django.contrib.messages.api import error
from django.core.exceptions import ValidationError
from .models import *
import re
from collections import Counter
from django.utils import timezone

class ContactForm(forms.Form):    
    email= forms.EmailField(max_length=50,required=False)
    name = forms.CharField(max_length=50,label='Họ và tên')
    messages = forms.CharField(widget= forms.Textarea, label='Lời nhắn')
    def clean_email(self):
        email = self.cleaned_data['email']
        time = timezone.now().date()
        contacts = Contact.objects.filter(email=email,createdate=time)
        count=1
        for contact in contacts:
            if(count >= 2):
                raise ValidationError('Địa chỉ email của bạn đã hết phiên phản hồi. Vui lòng nhập lại')
                break
            else:    
                count=count+1
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email):
            raise ValidationError('Email của bạn không hợp lệ. Vui lòng nhập lại')
        return email
    def clean_name(self):
        contacts=Contact.objects.all()
        name = self.cleaned_data["name"]
        if re.match(r'^\w+$',name):       
            raise ValidationError('Tên bạn có chứa kí tự đặt biệt. Vui lòng nhập lại')
        return name
    