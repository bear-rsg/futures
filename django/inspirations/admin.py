from django.contrib import admin
from . import models


def publish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish.short_description = "Publish selected inspirations (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish.short_description = "Unpublish selected inspirations (will not appear on main site)"


class InspirationAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Responses in the Django admin
    """
    list_display = ('inspiration_title',
                    'inspiration_text_preview',
                    'inspiration_image',
                    'inspiration_file',
                    'inspiration_video',
                    'inspiration_audio',
                    'inspiration_link',
                    'admin_published',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('admin_published', )
    search_fields = ('inspiration_title',
                     'inspiration_text',
                     'inspiration_file',
                     'inspiration_link',
                     'inspiration_video',
                     'inspiration_audio')
    list_per_page = 50
    ordering = ('inspiration_title', '-id')
    actions = (publish, unpublish)


# Register
admin.site.register(models.Inspiration, InspirationAdminView)
