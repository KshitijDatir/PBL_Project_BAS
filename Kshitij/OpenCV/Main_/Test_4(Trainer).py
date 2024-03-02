import cv2 as cv
import numpy as np
import os

import main_train_folder as mtf

DIR = r"Main_\Images_DB"


#Creating A File For Storing Each Person's Name:

def create_file(person):
   
    with open(r"Main_\DB_File\People","a+") as People_File:
        People_File.write(f"{person}\n") 
        index = len(People_File.readlines)

create_file()    
index = create_file.index

def make_list():

    with open(r"Main_\DB_file\People","r") as People_File:
        list=[]
        for line in People_File:
            list.append(line)
    return list
list = make_list()

mtf.main_train(DIR,list,person=None)
