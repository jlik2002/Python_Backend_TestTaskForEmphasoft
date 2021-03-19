
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView


urlpatterns = [
    path('user/',include('users.urls'))
]
