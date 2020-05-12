from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from dipno_backend.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) \
                + auth_admin.UserAdmin.fieldsets \
                + (("Dipno", {"fields": ("available_from", "available_to", )}),) \
                + (("Facebook", {"fields": ("facebook_id", "facebook_link", )}),)
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
