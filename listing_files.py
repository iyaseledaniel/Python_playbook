# How to access folders and files in directories
import  os
from datetime import datetime


def access_files(folder):
    for file in os.listdir(folder):
        print(file)
        get_files_attr(folder, file)
        if file.lower() == "downloads":
            access_files("d:/Downloads")
            get_files_attr("d:/Downloads", file)

def get_files_attr(folder, file):
    with os.scandir(folder) as dir:
        for entry in dir:
            if entry.name != file:
                continue
            else:
                #print(entry.name)
                file = entry
                if file:
                    #file_attr = file.stat().st_mtime
                    date_attr = datetime.fromtimestamp(file.stat().st_mtime).strftime("%d/%m/%Y %H:%M:%S")
                    print("Date Modified:", date_attr,"\n")
                break

    return file
access_files("d:/")