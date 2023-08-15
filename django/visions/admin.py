from django.contrib import admin
from . import models

admin.site.site_header = 'FUTURES: Admin Dashboard'


def approve(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to approved
    """
    queryset.update(admin_approved=True)


approve.short_description = "Approve selected visions (will appear on main site)"


def unapprove(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not approved
    """
    queryset.update(admin_approved=False)


unapprove.short_description = "Unapprove selected visions (will not appear on main site)"


class VisionAdditionalImageInline(admin.TabularInline):
    """
    A subform/inline form for VisionAdditionalImage to be used in VisionAdminView
    """
    model = models.VisionAdditionalImage
    extra = 0


class VisionAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Visions in the Django admin
    """
    list_display = ('vision_title',
                    'vision_text',
                    'vision_image',
                    'admin_approved',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('admin_approved',)
    list_per_page = 50
    ordering = ('-id',)
    inlines = (VisionAdditionalImageInline,)
    actions = (approve, unapprove)


def approve_response(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to approved
    """
    queryset.update(admin_approved=True)


approve_response.short_description = "Approve selected responses (will appear on main site)"


def disapprove_response(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not approved
    """
    queryset.update(admin_approved=False)


disapprove_response.short_description = "Disapprove selected responses (will not appear on main site)"


class ResponseAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Responses in the Django admin
    """
    list_display = ('__str__',
                    'vision',
                    'author_name',
                    'author_email',
                    'admin_approved',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('vision', 'admin_approved')
    search_fields = ('response_text', 'name')
    list_per_page = 30
    ordering = ('-id',)
    actions = (approve_response, disapprove_response)


# Register
admin.site.register(models.Response, ResponseAdminView)
admin.site.register(models.Vision, VisionAdminView)
