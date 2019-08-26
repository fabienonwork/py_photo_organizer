# PY Photo Organizer
This Python Project was created to help in organizing Pictures

This Script is moving pictures based on the meta tags to the correct Folders
Organized in following structure

    Year
    -> Month
    --> Day
    ---> DeviceModel
    ----> File
    
    #Example
    2019
    -> 08
    --> 22
    ---> SM-G955F
    ----> 20190822_184158.jpg
    

#### Requirements:
    # ubuntu
    sudo apt install python-pip
    sudo pip install exifread
    
    # in folder you want to execute the script please create a folder called 'pics_to_sort' where you put all your Pic's inside with folder or without
    mkdir pics_to_sort

#### Script has been tested under ubuntu18.04 & ubuntu16.04 but it is still in development can have bugs ;) 


