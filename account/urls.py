from django.urls import path
from account.views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
]
