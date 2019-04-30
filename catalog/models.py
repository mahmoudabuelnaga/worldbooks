from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
# Create your models here.

# Start Table type of literature
class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Genre,self).save(*args,**kwargs)
# End Table type of literature

# Start Table of authors
class Authers(models.Model):
    name                = models.CharField(max_length=200)
    slug                = models.SlugField(blank=True , null=True)
    img                 = models.ImageField(upload_to='auther_image/')
    date_of_publication = models.DateField(auto_now=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Authers,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-date_of_publication']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('auther-detail', args=[str(self.id)])
# End Table of authors

# Start Table of books
class Books(models.Model):
    title               = models.CharField(max_length=255)
    slug                = models.SlugField(blank=True , null=True)
    cover               = models.ImageField(upload_to='book_img/')
    pdf                 = models.FileField(upload_to='file_pdf/')
    summary             = models.TextField()
    auther              = models.ForeignKey(Authers,on_delete=models.SET_NULL , null=True)
    language            = models.CharField(max_length=100)
    genre               = models.ManyToManyField(Genre)
    date_of_publication = models.DateField(auto_now=True)
    famous_books        = models.BooleanField(default=False)
    tags                = models.CharField(max_length=300)

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Books,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-date_of_publication']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail' , args=[str(self.id)])
# End Table of books

# Start Table of Team
class Team(models.Model):
    name      = models.CharField(max_length=200)
    img       = models.ImageField(upload_to='team_img/')
    specialty = models.CharField(max_length=300)

    def __str__(self):
        return self.name
# End Table of Team
