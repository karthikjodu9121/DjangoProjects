from django.urls import path, include
from .views import app_home, author_details

urlpatterns = [
    path('', app_home, name = 'app_home'),
    path('apphome/', app_home, name = 'app_home'),
    path("AuthorDetails/", author_details, name = 'author_details')
]
