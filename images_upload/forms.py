from django import forms

from images_upload.models import Images


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ("image",)
