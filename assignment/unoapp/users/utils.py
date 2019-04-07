import smtplib
import uuid

from unoapp.settings import EMAIL_HOST_USER
from users.models import CustomUser, UserConfirmation
from django.core.mail import EmailMessage, send_mail


class Register():

    def __init__(self):
        pass


    def register1(self,email,password,fname,lname):
        newuser , is_created = CustomUser.objects.get_or_create(
            email = email.strip().lower(),
            password = password,
            first_name = fname,
            last_name = lname,
            username = email.strip().lower().replace('@','-')
        )

        if is_created:

            token = str(uuid.uuid1())
            user = CustomUser.objects.get(email =email.strip().lower())
            user_confirmation , is_created =UserConfirmation.objects.get_or_create(
                user_id =user.id,
                token = token
            )

            msg = 'Hey user please verify your email= ' +email+ " token= "+token.format(
            email=email,
            token=token
                )
            subject = 'Welcome to Test project'
            email = EmailMessage(
            subject=subject,
            body=msg,
            to=[email],
            from_email=EMAIL_HOST_USER,)
            email.send()


