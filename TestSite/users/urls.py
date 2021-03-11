
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('create/',views.CreateUserViewAPI.as_view()),
    path('authorization/',views.authenticate_user)
]

