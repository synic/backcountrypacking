import re

from django import http
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import FormView, ListView

from . import forms, models


def viewpage(request, path):
    path = re.sub(r'[^a-zA-Z0-9-]', '', path)
    page = get_object_or_404(models.Page, url=path)

    return render(request, 'dropcamp/page.html', {
        'page': page,
    })


class ContactView(FormView):
    template_name = 'dropcamp/contact.html'
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send()
        messages.info(
            self.request,
            "Your message has been sent, we will contact "
            "you soon."
        )
        return http.HttpResponseRedirect(reverse('dc:contact'))


class PackagesView(ListView):
    def get_queryset(self):
        return models.Package.objects.filter(
            type=self.kwargs['package_type'][:-1]).order_by('name')

    def get_template_names(self):
        return ('dropcamp/%s.html' % self.kwargs['package_type'],)
