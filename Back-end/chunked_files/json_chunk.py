import shutil
import os
import json


with open(newfile_path, 'r') as infile:
    o = json.load(infile)
    index = 0
    for i in range(0, len(o), size):
        with open(f"{folder_name}\file{index}.json".format(index), 'w') as outfile:
            index += 1
            json.dump(o[i:i + user_specified_size], outfile)