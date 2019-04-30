from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import BookFilter

urlpatterns=[
    path('', views.home, name='home'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authers/', views.AuthersListView.as_view(), name='authers'),
    path('auther/<slug:slug>/', views.AuthersDetailView.as_view(), name='auther-detail'),
    path('genre/', views.GenreListView.as_view(), name='genre'),
    path('genre/<slug:slug>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('contact/', views.emailView, name='contact'),
    path('search/' , FilterView.as_view(filterset_class=BookFilter,template_name='search/book_list_search.html'),name='search')
]
