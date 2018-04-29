from django.contrib import admin
from .models import Book, Discussion


# Register your models here.
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishdate', 'isbn', 'description', 'summary')
@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'datecreated', 'discussion', 'dateapproved')
