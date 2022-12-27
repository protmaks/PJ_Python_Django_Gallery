from django import forms
from django.views.generic.edit import CreateView

from .models import Image, Country

class ImageCreateView(CreateView):
    template_name = 'gallery/image_form_create.html'
    form_class = Image
    success_url = '/gallery/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countrys'] = Country.objects.all()
        return context