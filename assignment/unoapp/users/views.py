from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from django.contrib.auth.models import User, Group


# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser, UserConfirmation
from users.utils import Register


class registerAPI(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        email =request.data.get('email')
        password =request.data.get('password')
        fname =request.data.get('first_name')
        lname =request.data.get('last_name')
        if email and password and fname and lname:
            try:
                user = CustomUser.objects.get(email=email.strip().lower())
            except ObjectDoesNotExist as e:
                user =None
            if not user:
                    new_user =Register().register1(email,password,fname,lname)
                    return Response(data=[{"data":"A verification email has been sent on "+email}] ,status=status.HTTP_200_OK)

            else:
                    return Response(data=[{"message":"This email is already registred"}],status=status.HTTP_400_BAD_REQUEST)



        else:
                return Response(data=[{"message":"Details "}],status=status.HTTP_400_BAD_REQUEST)



class verifyemail(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        email = request.data.get('email')
        token = request.data.get('token')
        user = CustomUser.objects.get(email = email.strip().lower())

        confirm_user = UserConfirmation.objects.get(user_id=user.id)
        if confirm_user.token==token:
            user.is_verified =True
            user.save()
            return Response(data=[{"message":"Congratulations ! Your account has been verified"}],status=status.HTTP_200_OK)
        else:
            return Response(data=[{"message":"BAD request"}],status=status.HTTP_400_BAD_REQUEST)


class login(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self,request):
        email = request.data.get('email')
        # username = request.data.get('email')
        password = request.data.get('password')

        userobj = CustomUser.objects.get(email = email.strip().lower())
        user = authenticate(username='st.aakash-gmail.com', password='aakash')

        # user = authenticate(username =userobj.username.lower(),password =password)

        if user:

            return Response(data=[{"message":userobj.email}],status=status.HTTP_200_OK)
        else:

            return Response(data=[{"message":userobj.username}],status=status.HTTP_400_BAD_REQUEST)







