# Generated by Django 4.2.3 on 2023-08-15 07:17

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision_title', models.CharField(help_text='Required. Provide a short title to your vision.', max_length=255, verbose_name='Title')),
                ('vision_text', models.TextField(blank=True, help_text='Optional. Write about your vision.', null=True, verbose_name='Vision Text')),
                ('vision_link', models.URLField(blank=True, help_text='Optional. Must be a valid URL, e.g. https://www.birmingham.ac.uk', null=True, verbose_name='Vision Link')),
                ('vision_image', models.ImageField(blank=True, help_text='Optional. This main image of your vision will appear in the list of visions.', null=True, upload_to='visions/vision-images', verbose_name='Vision Image')),
                ('vision_video', embed_video.fields.EmbedVideoField(blank=True, help_text='Optional. Provide a URL of a video hosted on YouTube or Vimeo, e.g. https://www.youtube.com/watch?v=BHACKCNDMW8', null=True, verbose_name='Vision Video')),
                ('vision_audio', models.TextField(blank=True, help_text='Optional. Copy and paste the embed code from a SoundCloud file. E.g. &lt;iframe ... For help with this please visit: <a href="https://help.soundcloud.com/hc/en-us/articles/115003568008-Embedding-a-track-or-playlist" target="_blank">SoundCloud Help</a>', null=True, verbose_name='Vision Audio')),
                ('author_name', models.CharField(blank=True, help_text='Optional. Your name will be shown publicly alongside your vision.', max_length=255, null=True, verbose_name='Name')),
                ('author_email', models.EmailField(blank=True, help_text='Optional. Your email address will not be made publicly visible.', max_length=254, null=True, verbose_name='Email')),
                ('author_social', models.CharField(blank=True, help_text='Optional. Include a link to your social media profile, which will be shown publicly alongside your vision.', max_length=255, null=True, verbose_name='Social Media Profile')),
                ('admin_approved', models.BooleanField(default=False)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='last updated')),
            ],
            options={
                'ordering': ('-meta_created_datetime', 'id'),
            },
        ),
        migrations.CreateModel(
            name='VisionAdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='visions/vision-images')),
                ('vision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='additionalimages', to='visions.vision')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField()),
                ('response_image', models.ImageField(blank=True, null=True, upload_to='visions/response-images')),
                ('author_name', models.CharField(blank=True, help_text='Optional. Your name will be shown publicly alongside your vision.', max_length=255, null=True, verbose_name='Name')),
                ('author_email', models.EmailField(blank=True, help_text='Optional. Your email address will not be made publicly visible.', max_length=254, null=True, verbose_name='Email')),
                ('author_social', models.CharField(blank=True, help_text='Optional. Include a link to your social media profile, which will be shown publicly alongside your vision.', max_length=255, null=True, verbose_name='Social Media Profile')),
                ('admin_approved', models.BooleanField(default=False)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('vision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='visions.vision')),
            ],
            options={
                'ordering': ['-meta_created_datetime'],
            },
        ),
    ]
