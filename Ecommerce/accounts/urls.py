from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from accounts.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name = 'login')
]
