from rest_framework import generics,status,views,viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookModelSerializer


# Generic API Views

class BookListCreateGenericApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookRetrieveUpdateDeleteGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


# API Views

class BookListCreateApiView(views.APIView):

    def get(self,request):
        books=Book.objects.all()
        serialized_data=BookModelSerializer(books,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        serialized_data=BookModelSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)


class BookRetrieveUpdateDeleteApiView(views.APIView):

    def get(self,request,pk):
        book = get_object_or_404(Book,id=pk)
        serialized_data=BookModelSerializer(book)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        book = get_object_or_404(Book,id=pk)
        serialized_data=BookModelSerializer(instance=book,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        return Response(serialized_data.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book = get_object_or_404(Book,id=pk)
        book.delete()
        return Response({"Info":"The object was deleted."},status=status.HTTP_200_OK)


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
