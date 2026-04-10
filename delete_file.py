#program to delete files from a directory
import os

def delete_files(path):
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))
        print("Deleted file: " + file)

delete_files("")