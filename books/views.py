from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .models import Author, Genre, Condition, Book
from .serializers import (AuthorSerializer, GenreSerializer, ConditionSerializer,
                          BookCreateUpdateSerializer, BookListDetailSerializer,
                          BookUpdateReceiverSerializer)


class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ConditionDetailAPIView(generics.RetrieveAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class ConditionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListDetailSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListDetailSerializer


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BookUpdateReceiverAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateReceiverSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BookUpdateInterestAPIView(APIView):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book.interested_users.filter(pk=request.user.pk).exists():
            book.interested_users.remove(request.user)
        else:
            book.interested_users.add(request.user)
        data = BookListDetailSerializer(book, context={'request': request}).data
        return JsonResponse(data)
