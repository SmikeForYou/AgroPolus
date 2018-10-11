from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

urlpatterns = [
    path('sign-in/', obtain_jwt_token),
]