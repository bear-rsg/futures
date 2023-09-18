from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

admin.site.site_header = 'FutureVisions: Admin Dashboard'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Customise the admin interface: User
    """

    readonly_fields = ['date_joined', 'last_login']


# Unregister default Group
admin.site.unregister(Group)


# Register custom Group
@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    """
    Customise the admin interface: User
    """

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
