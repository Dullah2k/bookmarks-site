from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from account import views

urlpatterns = [
	path('admin/', admin.site.urls),
]
