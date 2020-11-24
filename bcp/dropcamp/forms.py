from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField()
    phone = forms.CharField(max_length=100, required=False)
    message = forms.CharField(max_length=5000, 
        widget=forms.Textarea(attrs={"cols": 30, "rows": 7}))

    def send(self):
        message = "%s\n%s\n%s\n\n%s" % (
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data.get('phone', 'No phone number specified'),
            self.cleaned_data['message'],
        )

        send_mail("New message from backcountrypacking contact form",
            message, self.cleaned_data['email'], 
            [settings.CONTACT_EMAIL], fail_silently=True)
