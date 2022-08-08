import shutil
import os
import json
from textwrap import indent
import math


class Bytfy_json:
    def __init__(self, file_path, user_specify_size, ):
        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.user_specify_size = user_specify_size
        self.folder_name = file_path.split(".")[0]
        

    def json_chunk(self,):
        size = math.ceil(self.file_size/self.user_specified_size)
        os.makedirs(self.folder_name)
        with open(self.file_path, 'r') as infile:
            o = json.load(infile,indent=4)
            index = 0
            for i in range(0, len(o), size):
                with open(f"{self.folder_name}\file{index}.json".format(index), 'w') as outfile:
                    index += 1
                    json.dump(o[i:i + self.user_specified_size], outfile)
            