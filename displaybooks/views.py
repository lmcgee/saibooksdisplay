from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from .models import Book, Discussion
from django.contrib.auth.decorators import login_required

# Create your views here.
#def index(request):
#    """
#    View function for home page for Sai Books.
#    """
#
#    num_books=Book.objects.all().count()
#
#    # Render the HTML template index.thml
#    return render(
#        request,
#        'home.html',
#        context={'num_books':num_books},
#    )

def home_page(request):
    """
        View function for home page for Sai Books.
        """

    num_books=Book.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.thml
    return render(
                  request,
                  'home.html',
                  context={'num_books':num_books,'num_visits':num_visits},
    )

def book_list(request):
    """
        View function for Book list!
    """
    books = Book.objects.all()
    post_comments = False
    commentpost = 'View_Comments'

    if request.method == 'POST':
        print(request.POST)

        if request.POST.get('commentpost') == 'View_Comments':
            commentpost = 'Hide_Comments'
            post_comments = True
        else:
            commentpost = 'View_Comments'
            post_comments = False
            return render(request,'displaybooks/book_list.html',  {'books':books,
            'post_comments':post_comments, 'commentpost':commentpost})

    return render(request,'displaybooks/book_list.html',  {'books':books,
     'post_comments':post_comments, 'commentpost':commentpost})

@login_required
def create_discussion(request):
    """
        Display the discussion form to receive user comments.
    """
    form = forms.DiscussionForm(request)
    if request.method == 'POST':
        form = forms.DiscussionForm(request.POST)
        if form.is_valid():
            discuss = form.save()
            send_mail(
                      'Discussion from{}'.format(form.cleaned_data['name']),
                      form.cleaned_data['discussion'],
                      '{name} <email>'.format(**form.cleaned_data),
                      ['gfmcgee@gwynfmcgee.com']
                      )
            messages.add_message(request, messages.SUCCESS,
                                     'Thanks for your discussion')
            return HttpResponseRedirect(reverse('discussion'))
    else:
        form = forms.DiscussionForm()
    return render(request, 'discussion_form.html', {'form': form})


def index1(request):
    """
    View function for homepage #2 Sai Book testing!
    """
    books = Book.objects.all()
    greeting='This is a test greeting for book1 changing the html pages.'
    return render(request, 'index1.html',  {'books':books})

def index2(request):
    """
    View function for homepage #2 Sai Book testing!
    """
    greeting='This is a test greeting for book2 changing the html pages.'
    #template = loader.get_template('index2') + {'greeting': greeting}
    context = {'greeting': greeting}
    return render(
        request,
        'index2.html',
        context,
    )

def index3(request):
    """
    View function for homepage #2 Sai Book testing!
    """
    greeting='This is a test greeting for book3 changing the html pages.'

    return render(
        request,
        'index3.html',
        context={'greeting': greeting},
    )
    
def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'displaybooks/discussion_list.html', {'discussions': discussions})
