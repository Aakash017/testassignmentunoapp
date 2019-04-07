from django.urls import path

from users.views import registerAPI, verifyemail, login

urlpatterns =[
        path('register/',registerAPI.as_view(),name = 'register'),
        path('verify-email/',verifyemail.as_view(),name = 'verify-email'),
        path('login/',login.as_view(),name = 'login'),


]
