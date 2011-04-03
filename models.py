from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=75)
    name_slug = models.SlugField()
    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=75)
    name_slug = models.SlugField()
    email = models.CharField(max_length=150, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    title_slug = models.SlugField()
    author = models.ForeignKey(Author, blank=True, null=True)
    is_loaned = models.BooleanField()
    loaned_to = models.ForeignKey(Person)
    have_read = models.BooleanField()
    started_reading = models.DateField(blank=True, null=True)
    when_finished = models.DateField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    bought_for = models.DecimalField(decimal_places=4, max_digits=8, blank=True, null=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/media/book/%s/%s" % (self.id, self.title_slug)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    title_slug = models.SlugField()
    is_loaned = models.BooleanField()
    loaned_to = models.ForeignKey(Person)
    have_watched = models.BooleanField()
    when_watched = models.DateField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    bought_for = models.DecimalField(decimal_places=4, max_digits=8, blank=True, null=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/media/movie/%s/%s" % (self.id, self.title_slug)