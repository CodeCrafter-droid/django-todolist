from django.urls import path
from . import views

urlpatterns = [
    path("",views.account,name="signup_login"),
    path("logout",views.logout_user,name="logout"),
]