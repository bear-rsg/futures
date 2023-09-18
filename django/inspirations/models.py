from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
import textwrap
import os


class Inspiration(models.Model):
    """
    A project-related inspiration, e.g. a PDF doc, image, or link.
    """

    inspiration_title = models.CharField(max_length=255)
    inspiration_text = RichTextField(blank=True, null=True)
    inspiration_image = models.ImageField(upload_to='inspirations-images', blank=True, null=True)
    inspiration_file = models.FileField(upload_to='inspirations-files', blank=True, null=True)
    inspiration_video = EmbedVideoField(blank=True, null=True)
    inspiration_link = models.URLField(blank=True, null=True)
    inspiration_audio = models.TextField(blank=True, null=True, help_text='Copy and paste the embed code from a SoundCloud file. E.g. &lt;iframe ... For help with this please visit: <a href="https://help.soundcloud.com/hc/en-us/articles/115003568008-Embedding-a-track-or-playlist" target="_blank">SoundCloud Help</a>')  # NOQA
    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    @property
    def inspiration_text_preview(self):
        return textwrap.shorten(self.inspiration_text, width=140, placeholder="...")

    @property
    def inspiration_file_name(self):
        return os.path.basename(self.inspiration_file.name)

    def __str__(self):
        return self.inspiration_title

    def save(self, *args, **kwargs):
        # Remove content after the iframe in soundcloud embed code
        if self.inspiration_audio and '<iframe' in self.inspiration_audio:
            self.inspiration_audio = self.inspiration_audio.split('</iframe>')[0] + '</iframe>'
        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['inspiration_title', '-id']
