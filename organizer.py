#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This Script is Moving pictures based on there metatags to the correct Folders
Orginzed in following structure
Year
->Month
-->Day
--->deviceModel
---->File

ScriptAuthor : MICHEL Fabien
ScriptVersion : 0.1
ScriptDate : 25 August 2019
@fabienonwork

Requirements:
    sudo apt install python-pip
    sudo pip install exifread
"""

import os
import exifread
import shutil

# Variables
path_to_scan = 'pics_to_sort'
path_to_notable = 'not_able_to_scan'
path_to_manual_verification = 'manual_verification_needed'
folder_creation_counter = int(0)
folder_removed_counter = int(0)
file_moved_counter = int(0)
fail_2move_counter = int(0)
files = []

# Class
class bcolors:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Functions
#CreateFolder
#   FirstParam      => Folder to create
#
def createFolder(folder_to_verify):
    global folder_creation_counter
    if not os.path.exists(folder_to_verify):
        os.makedirs(folder_to_verify)
        print(bcolors.WARNING+"Folder "+folder_to_verify+" has been created"+bcolors.ENDC)
        folder_creation_counter = folder_creation_counter+1
#CreateFolderEnd

#extrTime
#   FirstParam      => current File
#   SecondParam     => Model of Pic Device
#   TherdParam      => Date time of Pic
def extrTime(current_file,device_model,date_time):
    global file_moved_counter
    dateTime = str(date_time).split(" ")
    deviceModel = str(device_model).replace(" ", "")
    date = dateTime[0].split(":")
    time = dateTime[1].split(":")
    date_path = date[0]+"/"+date[1]+"/"+date[2]+"/"+deviceModel
    createFolder(date_path)
    try:
        shutil.move(current_file, date_path)
        print(bcolors.SUCCESS+"Moving \n From : "+current_file+"\n To : "+date_path+bcolors.ENDC)
        file_moved_counter = file_moved_counter+1
    except shutil.Error as e:
        print(bcolors.FAIL+"Error Message : \n"+str(e)+bcolors.ENDC)
        createFolder(path_to_manual_verification)
        shutil.move(current_file, path_to_manual_verification)
        print(bcolors.SUCCESS+"Moving \n From : "+current_file+"\n To : "+path_to_manual_verification+bcolors.ENDC)
#extrTimeEnd

# r=root, d=directories, f = files
for r, d, f in os.walk(path_to_scan):
    for file in f:
        files.append(os.path.join(r, file))
    for f in files:
        img = open(f)
        exif_data = exifread.process_file(img)
        try:
            model = exif_data['Image Model']
            date = exif_data['EXIF DateTimeOriginal']
            extrTime(f,model,date)
        except:
            createFolder(path_to_notable)
            try:
                shutil.move(f, path_to_notable)
                print(bcolors.SUCCESS+"Moving \n From : "+f+"\n To : "+path_to_notable+bcolors.ENDC)
            except:
                print(bcolors.FAIL+"An exception occured with file : "+str(f)+bcolors.ENDC)
            fail_2move_counter = fail_2move_counter+1
    for dire in d:
        if not os.listdir(r+"/"+dire):
            os.rmdir(r+"/"+dire)
            folder_removed_counter = folder_removed_counter+1

#Do some Stats Print
print("---")
print(bcolors.SUCCESS+"Created Folders: "+str(folder_creation_counter)+bcolors.ENDC)
print(bcolors.SUCCESS+"Removed Folders: "+str(folder_removed_counter)+bcolors.ENDC)
print(bcolors.SUCCESS+"Moved Files: "+str(file_moved_counter)+bcolors.ENDC)
print(bcolors.FAIL+"Not able to determin metatags: "+str(fail_2move_counter)+bcolors.ENDC)
