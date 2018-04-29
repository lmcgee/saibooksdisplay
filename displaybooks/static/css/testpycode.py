from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def product_form(request):
    form = forms.DigitalProductForm()
    if request.method == 'POST':
        form = forms.DigitalProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:create'))
    return render(request, 'products/product_form.html', {'form': form})