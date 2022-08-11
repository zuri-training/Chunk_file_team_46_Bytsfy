import shutil
import os
import json
from django.contrib import messages
from django.conf import settings
import math


class Bytfy_json:
    def __init__(self, file_path, user_specify_size, ):
        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.user_specify_size = user_specify_size
        self.folder_name = file_path.split(".")[0]


    def splitJSON(request):
 
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

    # def json_chunk(self,):
    #     size = math.ceil(self.file_size/self.user_specified_size)
    #     os.makedirs(self.folder_name)
    #     with open(self.file_path, 'r') as infile:
    #         o = json.load(infile,indent=4)
    #         index = 0
    #         for i in range(0, len(o), size):
    #             with open(f"{self.folder_name}\file{index}.json".format(index), 'w') as outfile:
    #                 index += 1
    #                 json.dump(o[i:i + self.user_specified_size], outfile)
            


def json_split(file_path):
    file_size = os.path.getsize(filename=file_path)
    file_name = file_name.split("/")[-1]
    with open(file_path) as json_file:
            data = json.load(json_file)
            data_length = len(data)

    print(data_length)
    print(file_size)
    # num_files = math.ceil(file_size/(user_specified_size))
    # split_data = [[] for i in range(0, num_files)]
    # starts = [math.floor(i * data_length/num_files) for i in range(0,num_files)]
    # starts.append(data_length)
    # folder_name = file_path.split(".")[0]
    # os.makedirs(folder_name)
    # for i in range(0,num_files):
    #     # loop through each range in array
    #     for n in range(starts[i],starts[i+1]):
    #         split_data[i].append(data[n])
        
    #     # create file when section is complete
        
    #     name = os.path.basename(file_name).split('.')[0] + '_' + str(i+1) + '.json'
    #     with open(f"{folder_name}/{name}", 'w') as outfile:
    #         json.dump(split_data[i], outfile, indent=4)


json_split("./simple.json")
