
from django.contrib import admin
from django.urls import include, path
#include needs to be brought in if we are going to bring in another urls.py file.

#Create routes
urlpatterns = [
    path('', include('pages.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
