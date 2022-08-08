import json
import math
import os
import sys
import shutil
from pathlib import Path
import pandas as pd

#TODO 1: bytify start first
#TODO 2: create split by line method
#TODO 2: create split by size method

def file_ext_name(file_path):
    """get extension name """
    file_name, ext = os.path.splitext(file_path)
    print(file_name) #check file name
    return (file_name, ext)



def user_spec_size():
    pass


"""""
Project bytfy: Bytsfy class that chunks bi json 
and csv files and into bits by bytes or lines by user specification
"""


"""""
Project bytfy: Bytsfy class that chunks bi json 
and csv files and into bits by bytes or lines by user specification
"""


class Bytfy_csv:
    # The Base Url file
    BASE_DIR = Path(__file__).resolve().parent.parent
    def __init__(self, uploaded_file, user_sepecif_size:int=None, per_lines:int=None, output_ext=".csv", doc_name=""):
        self.__accepted_fmt = (".csv", ".json") #added to chheck befor instance is created
        self.__file = uploaded_file
        self.file_name, self.file_ext = file_ext_name(self.file)
        self.file_size = os.path.getsize(uploaded_file)
        self.rows_per_file = per_lines
        self.chunk_limit = (20 * self.file_size) / 100
        self.user_specified_size = user_sepecif_size
        self.user_specified_ext = output_ext
        self.doc_name = doc_name
    @property
    def accepted_fmt(self):# will be at the backend
        return self.__accepted_fmt

    @property
    def file(self):
        return self.__file

    def __str__(self):
        return "You have uploaded {} with a {} extension".format(self.file, self.file_ext)

    def mkdir(self, filename):
            os.mkdir(f"{filename}")

    def remove_dir(self,):
        shutil.make_archive(self.file_name, "zip", self.file_name)
        shutil.rmtree(self.file_name) # path to the created dir

    def to_json(self, each_file, num):
        each_file.to_json(f"{self.file_name}\{self.doc_name}-{num}.json")
        # args[0].to_json(f"{self.file_name}\{args[1]}-{args[2]}.json")

    def to_csv(self, each_file, num):
        each_file.to_csv(f"{self.file_name}\{self.doc_name}-{num}.csv", index=False, index_label=False)
        # print(os.path.getsize(f"{self.file_name}-{num}.csv"))
        # print(type(f"{self.file_name}\{self.file_name}-{num}.csv"))

    def split_in_lines(self, to_json=False):
        # ext = self.file_name.split(".")[1]
        """"create a directory"""
        self.mkdir(self.file_name)
        num = 1
        for each_file in pd.read_csv(self.file, chunksize=self.rows_per_file):
            if not to_json:
                self.to_csv(each_file, num)
                # each_file.to_csv(f"customer_csv{k + 1}.csv")
            elif to_json:
                self.to_json(each_file,  num)# edited
            num += 1
                # each_file.to_json(f"customer_csv{k + 1}.json")
        self.remove_dir()
        return

    def csv_split(self, to_jsons=False):
        """check size if it is less than 5% of the total size"""
        if self.user_specified_size < self.chunk_limit:
            raise ValueError("please increase the size per file you want to chunk")
        # print(self.file_ext)
        """checking if file is an accepted fmt"""
        # if self.file_ext not in self.accepted_fmt:
        #     raise TypeError("Sorry input a an accepted format json or csv file")
        chunk_file_size = math.ceil(self.file_size / self.user_specified_size)
        total_length_of_file = len(pd.read_csv(self.file).index)
        row_per_file = math.ceil(total_length_of_file / chunk_file_size)
        print(row_per_file)
        num = 1
        """"create a directory"""
        self.mkdir(self.file_name)
        """"chunk files and move file to directory """
        for each_file in pd.read_csv(self.file, chunksize=row_per_file):
            if to_jsons == False:
                self.to_csv(each_file, num)
                # print(isinstance(filename, each_file))
            else:
                self.to_json(each_file,  num)# edited
            num += 1
            """"remove directory and zip directory"""
        self.remove_dir() # add path to the directory
        return

    def bytfy_start(self):
        """
        check file extention client wants, but by default the selection will be the
        uploaded file extension
        """

        """check if if the user wants to chunk by size or by rows per file"""


        if self.user_specified_ext == ".csv" and not isinstance(self.rows_per_file, int):
            self.csv_split()
        elif self.user_specified_ext == ".csv" and isinstance(self.rows_per_file, int):
            self.split_in_lines()
        elif self.user_specified_ext == ".json" and not isinstance(self.rows_per_file, int):
            self.csv_split(to_jsons=True)
        elif self.user_specified_ext == ".json" and isinstance(self.rows_per_file, int):
            self.split_in_lines(to_json=True)
        else:
            raise LookupError("sorry an error occured, kindly check your file or contact us")


 # def to_json(self, *args):
        # args[0].to_json(f"{self.file_name}\{args[1]}-{args[2]}.json")