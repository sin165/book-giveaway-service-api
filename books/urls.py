from django.urls import path

from . import views


urlpatterns = [
    path('authors/<int:pk>/', views.AuthorDetailAPIView.as_view(), name='author_detail'),
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author_list_create'),
    path('genres/<int:pk>/', views.GenreDetailAPIView.as_view(), name='genre_detail'),
    path('genres/', views.GenreListCreateAPIView.as_view(), name='genre_list_create'),
    path('conditions/<int:pk>/', views.ConditionDetailAPIView.as_view(), name='condition_detail'),
    path('conditions/', views.ConditionListCreateAPIView.as_view(), name='condition_list_create'),
    path('books/new/', views.BookCreateAPIView.as_view(), name='book_create'),
    path('books/', views.BookListAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', views.BookUpdateAPIView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteAPIView.as_view(), name='book_delete'),
    path('books/<int:pk>/update_interest/', views.BookUpdateInterestAPIView.as_view(), name='book_update_interest'),
    path('books/<int:pk>/update_receiver/', views.BookUpdateReceiverAPIView.as_view(), name='book_update_receiver'),
]
