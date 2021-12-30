from django.urls import path
from registerapp import views
urlpatterns=[
    path('',views.page),
    path('register/',views.register),
    path('login/',views.login),
    path('logon/',views.logpage)
]