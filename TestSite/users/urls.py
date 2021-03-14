
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('',views.HiPage),
    path('create/',views.CreateUserViewAPI.as_view()),
    path('authorization/',views.authenticate_user),
    path('get_me/',views.GetMe.as_view()),
    path('change/',views.Change.as_view()),
    path('remove/',views.Remove.as_view())
]

