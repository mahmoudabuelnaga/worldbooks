from django.contrib import admin
from .models import Authers,Books,Team,Genre
# Register your models here.
admin.site.register(Genre)
admin.site.register(Authers)
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','language','display_genre')
    list_filter = ['date_of_publication', 'famous_books']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','specialty')
