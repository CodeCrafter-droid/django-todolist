from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.account,name="signup_login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("delete",views.deleteacc,name="deleteacc"),
]