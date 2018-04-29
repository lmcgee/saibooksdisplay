from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from datetime import date, datetime, timedelta
from django_comments.moderation import CommentModerator, moderator

class Book(models.Model):
    """
        Model representing a book (but not a specific copy of a book).
        """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publishdate = models.DateField()
    description = models.TextField()
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    enable_comments = models.BooleanField()

    class Meta:
        ordering = ["-publishdate"]


    def __str__(self):
        """
            String for representing the Model object.
            """
        return self.title


    def get_absolute_url(self):
        """
            Returns the url to access a detail record for this book.
            """
        return reverse('book-detail', args=[str(self.id)])

class Discussion(models.Model):
    """
        Model representing a discussion item from a subscriber added to the database.
        """
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default="")
    email = models.EmailField()
    discussion = models.TextField(max_length=2000, help_text='Enter your comments here')
    approved = models.BooleanField(default=False)
    datecreated = models.DateField(default=datetime.now())
    dateapproved = models.DateField(null=True)

    class Meta:
        ordering = ["-datecreated"]


    def __str__(self):
        """
            String for representing the Model object.
            """
        return self.subject


    def get_absolute_url(self):
        """
            Returns the url to access a discussion record for this book.
            """
        return reverse('discussion', args=[str(self.id)])

class BookModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'

    moderator.register(Book, CommentModerator)
