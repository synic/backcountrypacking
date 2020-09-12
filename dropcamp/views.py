from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView
from django.contrib import messages
from django import http

from . import models
from . import forms

import re

def viewpage(request, path):
    path = re.sub(r'[^a-zA-Z0-9-]', '', path)
    page = get_object_or_404(models.Page, url=path) 

    return direct_to_template(request, 'dropcamp/page.html', {
        'page': page,
    })

class ContactView(FormView):
    template_name = 'dropcamp/contact.html'
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send()
        messages.info(self.request,
            "Your message has been sent, we will contact "
            "you soon.")
        return http.HttpResponseRedirect(reverse('dc:contact'))

class PackagesView(ListView):
    def get_queryset(self):
        return models.Package.objects.filter(
            type=self.kwargs['package_type'][:-1]).order_by('name')

    def get_template_names(self):
        return ('dropcamp/%s.html' % self.kwargs['package_type'],)
