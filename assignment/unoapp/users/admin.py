from django.contrib import admin

# Register your models here.
from users.models import CustomUser, UserConfirmation


class UserAdmin(admin.ModelAdmin):


    model = CustomUser
    list_display = ['email','username','first_name','last_name']


class UserConfirmationadmin(admin.ModelAdmin):
    model = UserConfirmation

    list_display = ['user',]

admin.site.register(CustomUser,UserAdmin)
admin.site.register(UserConfirmation,UserConfirmationadmin)
