from django.contrib import admin
from django.urls import path
from mychatapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat, name='chatbot')
]
