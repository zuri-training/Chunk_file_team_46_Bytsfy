import os.path
from django.shortcuts import render
from . import csv_chunk
from .models import UploadedFile
from django.contrib import messages
from pathlib import Path

# Create your views here.



def chunk(request):
    if request.method == 'POST':
        file_data = request.FILES["file"]

        if file_data.name.split(".")[-1] not in ("json", "csv"):
            messages.error(request, "Please upload csv or json file")

        base_dir = Path(__file__).parent.parent
        user_upload = UploadedFile(uploaded_file=request.FILES['file'])
        user_upload.save()
        name_of_file = user_upload.uploaded_file.name.split("/")#split
        newfile_path = os.path.join(base_dir, f"media\{name_of_file[0]}\{name_of_file[1]}")

        doc_name = name_of_file[-1].split(".")[0]
        if name_of_file[-1].split(".")[1] == "csv":
            bytfy = csv_chunk.Bytfy_csv(newfile_path, user_sepecif_size=100, output_ext=".csv", doc_name=doc_name)
            bytfy.bytfy_start()
        # user_upload.delete()
    return render(request, "upload.html")
#     return render(request, "dashboard")

