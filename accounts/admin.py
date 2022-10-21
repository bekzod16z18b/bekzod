from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('emal',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('emal',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
