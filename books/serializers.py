from rest_framework import serializers

from users.serializers import UserPublicSerializer
from .models import Author, Genre, Condition, Book


class AuthorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='author_detail',
        lookup_field='pk',
    )

    class Meta:
        model = Author
        fields = [
            'name',
            'url',
        ]


class GenreSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='genre_detail',
        lookup_field='pk',
    )

    class Meta:
        model = Genre
        fields = [
            'name',
            'url',
        ]


class ConditionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='condition_detail',
        lookup_field='pk',
    )

    class Meta:
        model = Condition
        fields = [
            'name',
            'url',
        ]


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'authors',
            'genres',
            'condition',
            'retrieval_info',
        ]


class BookUpdateReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['receiver']

    def validate(self, data):
        receiver = data['receiver']
        instance = getattr(self, 'instance', None)
        interested_users = instance.interested_users.all()
        if receiver not in interested_users:
            raise serializers.ValidationError("receiver must be in interested users")
        return data


class BookListDetailSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only=True)
    authors = serializers.SerializerMethodField(read_only=True)
    genres = serializers.SerializerMethodField(read_only=True)
    condition = serializers.SerializerMethodField(read_only=True)
    interested_users = serializers.SerializerMethodField(read_only=True)
    receiver = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'authors',
            'genres',
            'condition',
            'owner',
            'retrieval_info',
            'interested_users',
            'receiver',
        ]
    
    def get_authors(self, obj):
        return AuthorSerializer(obj.authors, many=True, context=self.context).data
    
    def get_genres(self, obj):
        return GenreSerializer(obj.genres, many=True, context=self.context).data
    
    def get_condition(self, obj):
        return ConditionSerializer(obj.condition, context=self.context).data
    
    def get_interested_users(self, obj):
        return UserPublicSerializer(obj.interested_users, many=True, context=self.context).data
    
    def get_receiver(self, obj):
        return UserPublicSerializer(obj.receiver, context=self.context).data
