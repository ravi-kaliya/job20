from django import forms
from upload.models import Uploads,UploadsFiles


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'


class UploadsFilesForm(forms.ModelForm):
    class Meta:
        model = UploadsFiles
        fields = '__all__'