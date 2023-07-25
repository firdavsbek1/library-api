from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Library API for non business company",
        terms_of_service='Good to go',
        contact=openapi.Contact(email='jalolov.firdavs0809@gmai.com'),
        license=openapi.License('library licence')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('books.urls')),
    # path("allauth/accounts/",include('allauth.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),

    # swagger
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0)),
    path('docs/',schema_view.with_ui('redoc',cache_timeout=0)),

]
