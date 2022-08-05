import os.path
from django.shortcuts import render
from . import csv_chunk
from .forms import Uploaded_file
from pathlib import Path

# Create your views here.


def chunk(request):
    if request.method == "POST":
        # Path(__file__).parent.parent
        base_dir = os.getcwd()
        user_upload = Uploaded_file(uploaded_file=request.FILES['file'])
        user_upload.save()
        name_of_file = user_upload.uploaded_file.name.split("/")#split
        newfile_path = os.path.join(base_dir, fr"chunked_files\{name_of_file[0]}\{name_of_file[1]}")
        # print(base_dir)
        print("----------------")
        doc_name = name_of_file[-1].split(".")[0] # pure document name
        print(name_of_file[-1].split(".")[0])
        print("----------------")
        # print(csv_chunk.file_ext_name(newfile_path))
        bytes =csv_chunk.Bytfy_csv(newfile_path, user_sepecif_size=100, output_ext=".csv", doc_name=doc_name)
        bytes.bytfy_start()
        user_upload.delete()

    return render(request, "upload.html")