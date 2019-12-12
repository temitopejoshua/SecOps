from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Elders, Natives, Citizens,Activities, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name']


admin.site.register(Elders)
admin.site.register(Natives)
admin.site.register(Citizens)
admin.site.register(Activities)
admin.site.register(CustomUser, CustomUserAdmin)
