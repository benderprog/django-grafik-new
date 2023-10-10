from django.urls import path
from .views import peoples_list



urlpatterns = [
    path("", peoples_list),
]