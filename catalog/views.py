from django.shortcuts import render, redirect,get_object_or_404
from .models import Authers,Books,Team,Genre
from django.views.generic import ListView,DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    num_books   = Books.objects.all().count()
    num_authers = Authers.objects.all().count()
    books       = Books.objects.filter(famous_books=True)
    team        = Team.objects.all()
    context = {
        'num_books'   : num_books,
        'num_authers' : num_authers,
        'books'       : books,
        'team'        : team,
    }
    return render(request,'home.html',context)

class BookListView(ListView):
    model               = Books
    context_object_name = 'books_list'
    template_name       = 'catalog/books.html'
    paginate_by         = 32

class BookDetailView(LoginRequiredMixin,DetailView):
    model               = Books
    template_name       = 'catalog/book_detail.html'
    context_object_name = 'book'
    login_url           = 'login'

class AuthersListView(ListView):
    model               = Authers
    context_object_name = 'authers_list'
    template_name       = 'catalog/authers.html'
    paginate_by         = 32
    def Query_set(self):
        return Books.objects.filter(Authers=auther).count()

class AuthersDetailView(LoginRequiredMixin,DetailView):
    model               = Authers
    context_object_name = 'auther'
    template_name       = 'catalog/auther_detail.html'
    login_url           = 'login'

class GenreListView(ListView):
    model               = Genre
    context_object_name = 'genre_list'
    template_name       = 'catalog/genre.html'
    paginate_by         = 32
    def Query_set(self):
        return Books.objects.filter(Genre=genre).count()

class GenreDetailView(LoginRequiredMixin,DetailView):
    model               = Genre
    context_object_name = 'genre'
    template_name       = 'catalog/genre_detail.html'
    login_url           = 'login'

def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject    = form.cleaned_data['subject']
            email      = form.cleaned_data['email']
            message    = form.cleaned_data['message']
            try:
                send_mail(subject+email, message, email,['worldofbooks1751998@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})
