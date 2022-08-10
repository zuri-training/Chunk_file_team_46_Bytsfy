from django import forms
from .models import Uploaded_file


class ChunkForm(forms.Form):
    # the chunk size is to determine how the file is going to be chunked
    file = forms.FileField()
    chunk_size = forms.IntegerField()


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    class Meta:
        model = Uploaded_file
