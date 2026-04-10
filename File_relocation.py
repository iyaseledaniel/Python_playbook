#!/usr/bin/env python3
"""This program walks through directory d:/downloads,
   finds files ending with their corresponding extension as outlined in the dictionary{.mp4,.pdf,.srt}
   creates directories using the dictionary key:value relationship,
   then moves them to their corresponding destination folder
"""

import os
import shutil
from pathlib import Path


def copy_file(src, dst):
    """Function to copy a file from src: source path to dst: destination path"""
    for file in os.listdir(src):  # walks through files in src(D:/downloads)

        if os.path.isfile(os.path.join(src, file)):  # checks if source file is a file and not directory
            # print(file)
            full_path_obj = Path(os.path.join(src, file))  # gets current file's path including extension
            extension = full_path_obj.suffix  # get file extension(.mp4 etc)

            if file.endswith(
                    extension) and extension in dst.keys():  # checks file extension and if extension exist in dictionary
                dst_path = str(dst.get(extension))  # set destination path using dictionary key:value relationship

                if not os.path.exists(dst_path):  # checks if destination folder does not exist
                    os.makedirs(dst_path, exist_ok=True)  # creates folder

                full_path = os.path.join(src, full_path_obj.name)
                if os.path.isfile(full_path):
                    dst_file = [file for file in os.listdir(dst_path)]
                    # print(dst_file)
                    if file in dst_file:
                        print(file + " already exists")
                    else:
                        shutil.move(full_path, dst_path)
                        print(file + f" file moved to " + dst_path)
            else:
                # executes else if extension does not exist in dictionary
                print(f"Would you like to create a folder for {extension} files", end=",")
                response = input("Y/N:")
                if response.upper() == "Y":
                    new_folder_name = input("Enter new folder name: ")
                    dest_path = os.path.join("D:/Downloads/", new_folder_name)
                    try:
                        if not os.path.exists(dest_path):
                            os.makedirs(dest_path, exist_ok=True)
                    except Exception as e:
                        print("Error: ", e)
                    full_path = os.path.join(src, full_path_obj.name)
                    try:
                        if os.path.isfile(full_path):
                            dest_file = [file for file in os.listdir(dest_path)]
                            if file in dest_file:
                                print(file +" already exists")
                            else:
                                shutil.move(full_path, dest_path)
                                print(file + f" file moved to " + dest_path)
                    except Exception as e:
                        print("Error: ", e)

                continue
        else:
            continue


destination = {
    '.mp4': "D:/Downloads/videos",
    '.pdf': "D:/Downloads/Pdf_files",
    '.srt': "D:/Downloads/Subtitles",
    '.exe': "D:/Downloads/Applications"
}
copy_file("D:/Downloads", destination)
