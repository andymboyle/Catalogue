from django.contrib import admin
from catalog.stuff.models import Author, Book, Movie, Person

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title', ) }
    search_fields = ['title']

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name_slug': ('name', ) }
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)