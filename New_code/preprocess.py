#Deleting blank lines
#Needs to be located in the folder of outputs

from os import listdir
from os.path import isfile, isdir
import os  


def ls1(path):
    return [obj for obj in listdir(path) if isfile(path + obj)]

save_path= "/home/lzanella/open-sesame/"
files=ls1(save_path+"Original texts/")

for file in files: 
    file1 = os.path.join(save_path+"Original texts/"+file)
    with open(file1,"r") as f, open("t"+file,"w") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:              
                outfile.write(i)
