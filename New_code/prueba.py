from os import listdir
from os.path import isfile, isdir
import sesame


def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

files=ls1("/home/lzanella/RDD_corpus/Corpus/Original texts/")

for file in files:
	targetid --mode predict \
                            --model_name fn1.7-pretrained-targetid \
                            --raw_input file
