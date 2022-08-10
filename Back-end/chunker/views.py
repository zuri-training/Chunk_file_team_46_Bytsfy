from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from .models import File, User
import pandas as pd
from django.contrib import messages
import shutil
import os
import math
import json
import csv

# Create your views here.
# ******************* HOME VIEW *****************************
def homePage(request):
    if request.user.is_authenticated:
        user = request.user
        allfile = user.file_set.all()
        context = {"allfile": allfile}

        return render(request, "home.html", context)

    return render(request, "home.html") 


def splitCSV(request):
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

        if file_path.split(".")[-1] == 'csv': 
            
            file_size = os.path.getsize(file_path)

            try:
                no_file_row = len(pd.read_csv(file_path)) - 1

                no_of_chuncked_file = math.ceil(file_size/user_specified_size)
                chunksize_user_specified_size = math.ceil(no_file_row/no_of_chuncked_file)
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
                for chunk in pd.read_csv(file_path, chunksize=chunksize_user_specified_size):
                    chunk.to_csv(f"{folder_name}/file{index}.csv".format(index), index=False)
                    index += 1

                # live server
                fs = folder_name.split("/")[-1]
                # local host
                # fs = folder_name.split("\\")[-1]
                outputfile = str(settings.MEDIA_ROOT) + f"/{fs}"
                
                shutil.make_archive(outputfile, 'zip', folder_name)
                shutil.rmtree(folder_name)
                zip_file_name = f"{fs}.zip"
                #local host
                # zip_file = f"/{outputfile}.zip"
                # live server
                zip_file = f"/{outputfile.split('/')[-1]}.zip"
                file= File.objects.create(user=request.user, file_name=zip_file_name, zip_file=zip_file)
                file.save()
                os.remove(file_path)
                context = {"file": file}
                # context  = {}
                return render(request, "splitcsv.html", context)

            except:
                messages.error(request, "Please upload a valid csv file")
                return redirect(request.META.get("HTTP_REFERER"))
   
    return render(request, "splitcsv.html")

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
        fs = folder_name.split("/")[-1]
        # local host
        # fs = folder_name.split("\\")[-1]
        outputfile = str(settings.MEDIA_ROOT) + f"/{fs}"
        
        shutil.make_archive(outputfile, 'zip', folder_name)
        shutil.rmtree(folder_name)
        zip_file_name = f"{fs}.zip"
        #local host
        # zip_file = f"/{outputfile}.zip"
        # live server
        zip_file = f"/{outputfile.split('/')[-1]}.zip"
        file= File.objects.create(user=request.user, file_name=zip_file_name, zip_file=zip_file)
        file.save()
        os.remove(file_path)
        context = {"file": file}
        # context  = {}
        return render(request, "splitcsv.html", context)


    context = {}
    return render(request, "splitjson.html", context)

def save(request, pk):
    file = File.objects.get(id=pk)
    file.saved_file = file.zip_file
    file.save()
    return HttpResponse("File saved successsfully")

def delete(request, pk):
    file = File.objects.get(id=pk)
    file.delete()
    return HttpResponse("File deleted successsfully")




def csvToJson(request):
    if request.method == "POST":
        csv_file = request.FILES["CSVfile"]
        json_file_name = csv_file.name.split(".")[0] + "-json-file.json"
        file_name = default_storage.save(csv_file.name, csv_file)
        file_path = default_storage.path(file_name)
        json_array= []
        
        json_path = f"{settings.MEDIA_ROOT}/{json_file_name}"
        with open(file_path, encoding="utf-8") as csv_file_handler:
            csv_reader = csv.DictReader(csv_file_handler)
            for rows in csv_reader:
                json_array.append(rows)
        with open(json_path, 'w', encoding="utf-8") as json_file_handler:
            json_file_handler.write(json.dumps(json_array, indent=4))
        json_file = json_path.split("/")[-1]
        file = File.objects.create(user=request.user, file_name=json_file_name, zip_file=json_file)
        file.save()
        os.remove(file_path)
        context = {"file": file}
        return render(request, "csvToJson.html", context)
    context = {}
    return render(request, "csvToJson.html", context)


def jsonToCsv(request):
    return HttpResponse("Under construction")
