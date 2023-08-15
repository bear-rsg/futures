from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.utils.text import Truncator
from embed_video.fields import EmbedVideoField
import textwrap
import logging

logger = logging.getLogger(__name__)
MEDIA_DIR_VISION_IMAGES = 'visions/vision-images'


class Vision(models.Model):
    """
    A user uploaded vision of the future
    """

    # Vision fields
    vision_title = models.CharField(max_length=255, help_text="Required. Provide a short title to your vision.", verbose_name='Title')
    vision_text = models.TextField(blank=True, null=True, help_text="Optional. Write about your vision.", verbose_name='Vision Text')
    vision_link = models.URLField(blank=True, null=True, help_text='Optional. Must be a valid URL, e.g. https://www.birmingham.ac.uk', verbose_name='Vision Link')
    vision_image = models.ImageField(upload_to=MEDIA_DIR_VISION_IMAGES, blank=True, null=True, help_text="Optional. This main image of your vision will appear in the list of visions.", verbose_name='Vision Image')
    vision_video = EmbedVideoField(blank=True, null=True, help_text='Optional. Provide a URL of a video hosted on YouTube or Vimeo, e.g. https://www.youtube.com/watch?v=BHACKCNDMW8', verbose_name='Vision Video')
    vision_audio = models.TextField(blank=True, null=True, help_text='Optional. Copy and paste the embed code from a SoundCloud file. E.g. &lt;iframe ... For help with this please visit: <a href="https://help.soundcloud.com/hc/en-us/articles/115003568008-Embedding-a-track-or-playlist" target="_blank">SoundCloud Help</a>', verbose_name='Vision Audio')
    # Author fields
    author_name = models.CharField(max_length=255, blank=True, null=True, help_text='Optional. Your name will be shown publicly alongside your vision.', verbose_name='Name')
    author_email = models.EmailField(blank=True, null=True, verbose_name='Email', help_text='Optional. Your email address will not be made publicly visible.')
    author_social = models.CharField(blank=True, null=True, max_length=255, help_text='Optional. Include a link to your social media profile, which will be shown publicly alongside your vision.', verbose_name='Social Media Profile')
    # Admin fields
    admin_approved = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="last updated")

    @property
    def vision_text_preview(self):
        return textwrap.shorten(self.vision_text, width=140, placeholder="...")

    @property
    def vision_link_html(self):
        return f'<a href="{self.vision_link}" target="_blank">{self.vision_link}</a>'

    def __str__(self):
        return f'Vision #{self.id} - {str(self.meta_created_datetime)[:19]}: {Truncator(self.vision_text).chars(50)}'

    def save(self, *args, **kwargs):

        # Remove content after the iframe in soundcloud embed code
        if self.vision_audio and '<iframe' in self.vision_audio:
            self.vision_audio = self.vision_audio.split('</iframe>')[0] + '</iframe>'

        # Email the research team when a new object is saved
        # Only send if this is a newly created object and not in debug
        if self.meta_created_datetime is None and settings.DEBUG is False:
            try:
                send_mail('FUTURES: A new vision has been shared',
                          'There has been a new vision submitted to the FUTURES website.',
                          settings.DEFAULT_FROM_EMAIL,
                          settings.NOTIFICATION_EMAIL,
                          fail_silently=False)
            except Exception:
                logger.exception("Failed to send email")

        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-meta_created_datetime', 'id')


class VisionAdditionalImage(models.Model):
    """
    An additional image associated with a vision
    """

    vision = models.ForeignKey(Vision, related_name='additionalimages', on_delete=models.PROTECT)
    image = models.ImageField(upload_to=MEDIA_DIR_VISION_IMAGES)

    def __str__(self):
        return f'{self.vision}: Image {self.image}'


class Response(models.Model):
    """
    The response that a user submits in response to a vision
    """

    # Vision fields
    vision = models.ForeignKey(Vision, related_name='responses', on_delete=models.PROTECT)
    # Response fields
    response_text = models.TextField()
    response_image = models.ImageField(upload_to='visions/response-images', blank=True, null=True)
    # Author fields
    author_name = models.CharField(max_length=255, blank=True, null=True, help_text='Optional. Your name will be shown publicly alongside your vision.', verbose_name='Name')
    author_email = models.EmailField(blank=True, null=True, verbose_name='Email', help_text='Optional. Your email address will not be made publicly visible.')
    author_social = models.CharField(blank=True, null=True, max_length=255, help_text='Optional. Include a link to your social media profile, which will be shown publicly alongside your vision.', verbose_name='Social Media Profile')
    # Admin fields
    admin_approved = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="created")
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="last updated")

    def __str__(self):
        return f'Response #{self.id} - {str(self.meta_created_datetime)[:19]}: {Truncator(self.response_text).chars(50)}'

    def save(self, *args, **kwargs):
        """
        Email the research team when a new object is saved
        """

        # Only send if this is a newly created object and not in debug
        if self.meta_created_datetime is None and settings.DEBUG is False:
            try:
                send_mail('FUTURES: A new response to a vision has been shared',
                          'There has been a new response to a vision submitted to the FUTURES website.',
                          settings.DEFAULT_FROM_EMAIL,
                          settings.NOTIFICATION_EMAIL,
                          fail_silently=False)
            except Exception:
                logger.exception("Failed to send email")

        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-meta_created_datetime']
