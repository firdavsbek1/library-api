from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from .models import Book, User


class UserModelSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username',)


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'isbn', 'rating', 'price')

    # def validate(self, data):
    #     title = data.get('title')
    #     if Book.objects.filter(title=title, author=data.get('author')).exists():
    #          raise ValidationError({
    #             'error': "The information provided already in the database!"
    #         }, )
    #     return data

    def validate_price(self, price):
        print(price)
        if price<=0 or price>=100:
            raise ValidationError({
                'error': "The price is out of range!"
            })
        return price
