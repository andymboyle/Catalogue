from django.contrib import admin
from firetracker.fires.models import Author, Book, Movie

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Movie, MovieAdmin)