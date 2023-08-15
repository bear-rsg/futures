from django import forms
from . import models
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class VisionCreateForm(forms.ModelForm):
    """
    Form to specify fields in the Vision create form
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Vision
        fields = (
            'vision_title',
            'vision_text',
            'vision_link',
            'vision_image',
            'vision_video',
            'vision_audio',
            'author_name',
            'author_email',
            'author_social'
        )


class ResponseCreateForm(forms.ModelForm):
    """
    Form to specify fields in the Response create form
    """

    response_text = forms.CharField(max_length=1000,
                                    widget=forms.Textarea(),
                                    label='Your response')
    response_image = forms.ImageField(label='Upload image',
                                      help_text='Optional',
                                      required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Response
        fields = (
            'response_text',
            'response_image',
            'author_name',
            'author_email',
            'author_social',
            'vision'
        )
