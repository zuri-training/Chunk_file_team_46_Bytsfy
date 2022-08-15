from textwrap import indent
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from .models import File, User
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.contrib import messages
import shutil
import os
import math
import json
import csv

# Create your views here.

@login_required(login_url="account_login")
def splitCSV(request):
    if request.method == 'POST':
        if not request.FILES["file"]:# checking if the upload is empty
            messages.error(request, "upload a file")
        file_data = request.FILES["file"]
        split_type = request.POST.get("splittype") # get the split type
        output_csv = request.POST.get("customRadio")
        output_json = request.POST.get("customRadio1")
        print(bool(request.POST["byline"]))
        print(bool(request.POST["chunk_size"]))
        print("csv",output_csv)
        print("json",output_json)
        print(split_type)
        if bool(request.POST["chunk_size"]):
            print("hi")

        
        if file_data.name.split(".")[-1] not in ["json","csv"]:
            messages.error(request, "Please upload csv or json file")
            return redirect(request.META.get("HTTP_REFERER"))

        try:
            if bool(request.POST["chunk_size"]): # check if the chunk size has a value
                user_specified_size = int(request.POST["chunk_size"])

            elif bool(request.POST["byline"]):
                by_line = int(request.POST["byline"]) # check if the user specified by line chunk
                used_size = by_line
        except:
             messages.error(request, "invalid size")
             return redirect(request.META.get("HTTP_REFERER"))

        file_name = default_storage.save(file_data.name, file_data)
        file_name = file_name.split("/")[-1]
        file_path = default_storage.path(file_name)

        if file_path.split(".")[-1] == 'csv': 
            
            file_size = os.path.getsize(file_path)
            model_file_size = math.ceil(file_size/1024)

            try:
                no_file_row = len(pd.read_csv(file_path)) - 1

                no_of_chuncked_file = math.ceil(file_size/user_specified_size)
                chunksize_user_specified_size = math.ceil(no_file_row/no_of_chuncked_file) * 1000
                used_size = chunksize_user_specified_size if bool(request.POST["chunk_size"]) else by_line # if user selects bysize
                print("tis is the used line", used_size)
                if bool(request.POST["chunk_size"]): # check if user put chunk size
                    if user_specified_size >= file_size:
                        messages.error(request, "chunk size cannot be equal to or greater than file size")
                        return redirect(request.META.get("HTTP_REFERER"))
                
                # file size should be 200mb or less 
                # if file_size > 200000000:
                #     messages.error(request, "chunk size must be more than 20percent file size ")
                #     return redirect(request.META.get("HTTP_REFERER"))
                # chunk size to be 20% or more of file size
                # chunk_limit = (0.2)*file_size
                # if chunk_limit > user_specified_size:
                #     messages.error(request, "chunk size must be more than 20percent file size ")
                #     return redirect(request.META.get("HTTP_REFERER"))
                
                folder_name = file_path.split(".")[0]
                os.makedirs(folder_name)
                index = 0
                for chunk in pd.read_csv(file_path, chunksize=used_size):
                    if output_csv is not None: # if the out put is csv
                        chunk.to_csv(f"{folder_name}/file{index}.csv".format(index), index=False)
                    else: # else chunk to json
                        chunk.to_json(f"{folder_name}/file{index}.json".format(index), indent=2)
                    index += 1

                # live server
                # fs = folder_name.split("/")[-1]
                # local host
                fs = folder_name.split("\\")[-1]
                outputfile = str(settings.MEDIA_ROOT) + f"/{fs}"
                
                shutil.make_archive(outputfile, 'zip', folder_name)
                shutil.rmtree(folder_name)
                zip_file_name = f"{fs}.zip"
                #local host
                zip_file = f"/{outputfile}.zip"
                # live server
                # zip_file = f"/{outputfile.split('/')[-1]}.zip"
                file= File.objects.create(user=request.user, file_size = model_file_size, file_name=zip_file_name, zip_file=zip_file)
                file.save()
                os.remove(file_path)
                return redirect("download-save", pk=file.id)

            except:
                messages.error(request, "Please upload a valid csv file")
                return redirect(request.META.get("HTTP_REFERER"))
   
    return render(request, "csv.html")


@login_required(login_url="account_login")
def splitJSON(request):
    if request.method == 'POST':
        file_data = request.FILES["file"]

        if file_data.name.split(".")[-1] not in ["json","csv"]:
            messages.error(request, "Please upload csv or json file")
            return redirect(request.META.get("HTTP_REFERER"))
        
        try:
            user_specified_size = request.POST["chunk_size"]
            user_specified_size = int(user_specified_size)
        except:
             messages.error(request, "invalid size")
             return redirect(request.META.get("HTTP_REFERER"))
            
        
            
        file_name = default_storage.save(file_data.name, file_data)
        file_name = file_name.split("/")[-1]
        file_path = default_storage.path(file_name)

        if file_path.split(".")[-1] == 'json': 
            file_size = os.path.getsize(file_path)
            if user_specified_size >= file_size:
                messages.error(request, "chunk size cannot be equal to or greater than file size")
                return redirect(request.META.get("HTTP_REFERER"))
            with open(file_path) as json_file:
                data = json.load(json_file)
                try:
                    data_length = len(data)
                except:
                    messages.error(request, "Invalid json file")
                    return redirect(request.META.get("HTTP_REFERER"))
        num_files = math.ceil(file_size/(user_specified_size))
        split_data = [[] for i in range(0,num_files)]
        starts = [math.floor(i * data_length/num_files) for i in range(0,num_files)]
        starts.append(data_length)
        folder_name = file_path.split(".")[0]
        os.makedirs(folder_name)
        for i in range(0,num_files):
            # loop through each range in array
            for n in range(starts[i],starts[i+1]):
                split_data[i].append(data[n])
            
            # create file when section is complete
            
            name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
            with open(f"{folder_name}/{name}", 'w') as outfile:
                json.dump(split_data[i], outfile, indent=4)

        # live server
        # fs = folder_name.split("/")[-1]
        # local host
        fs = folder_name.split("\\")[-1]
        outputfile = str(settings.MEDIA_ROOT) + f"/{fs}"
        
        shutil.make_archive(outputfile, 'zip', folder_name)
        shutil.rmtree(folder_name)
        zip_file_name = f"{fs}.zip"
        #local host
        zip_file = f"/{outputfile}.zip"
        # live server
        # zip_file = f"/{outputfile.split('/')[-1]}.zip"
        file= File.objects.create(user=request.user, file_name=zip_file_name, zip_file=zip_file)
        file.save()
        os.remove(file_path)
        return redirect("download-save", pk=file.id)


    return render(request, "json.html")


@login_required(login_url="account_login")
def save(request, pk):
    file = File.objects.get(id=pk)
    file.saved_file = file.zip_file
    file.save()
    return redirect('dashboard')


@login_required(login_url="account_login")
def delete(request, pk):
    file = File.objects.get(id=pk)
    file.delete()
    return redirect('dashboard')


@login_required(login_url="account_login")
def dashboard(request):
    user = request.user
    files = user.file_set.all()
    context = {'files': files}
    return render(request, 'Saved_Files.html', context)


@login_required(login_url="account_login")
def downloadFile(request, pk):
    file = File.objects.get(id=pk)
    context = {"file": file}
    return render(request, "downloadfile.html", context) 
