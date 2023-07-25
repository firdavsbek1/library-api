from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import BookListCreateApiView,BookRetrieveUpdateDeleteApiView,BookModelViewSet

router=DefaultRouter()
router.register(r'router/books',BookModelViewSet,basename='books')

urlpatterns = [
    path('books/',BookListCreateApiView.as_view()),
    path('books/<int:pk>/',BookRetrieveUpdateDeleteApiView.as_view()),

]

urlpatterns+=router.urls