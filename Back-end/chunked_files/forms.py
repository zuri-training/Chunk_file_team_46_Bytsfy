from django import forms


class ChunkForm(forms.Form):
    # the chunk size is to determine how the file is going to be chunked
    file = forms.FileField()
    chunk_size = forms.IntegerField()
