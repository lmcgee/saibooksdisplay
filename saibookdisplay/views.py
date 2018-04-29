from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')

def discussion_view(request):
    form = forms.DiscussionForm()
    if request.method == 'POST':
        form = forms.DiscussionForm(request.POST)
        if form.is_valid():
            send_mail(
                      'Discussion from{}'.format(form.cleaned_data['name']),
                      form.cleaned_data['discussion'],
                      '{name} <email>'.format(**form.cleaned_data),
                      ['gfmcgee@gwynfmcgee.com']
                      )
                      messages.add_message(request, messages.SUCCESS,
                                           'Thanks for your discussion')
                      return HttpResponseRedirect(reverse('discussion'))
    return render(request, 'discussion_form.html', {'form': form})
