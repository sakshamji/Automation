import os
import shutil
def create_folders(path):
    folder_names = ["Audio","Video","Text","PDFs","Zips","Executable Files","Images","Other files","Other folders"]
    for folders in folder_names:
        try:
            os.mkdir(os.path.join(path, folders) )
        except:
            continue

def send_files(files,path):
    folder_names = ["Audio","Video","Text","PDFs","Zips","Executable Files","Images","Other files","Other folders"]
    for f in files:
        if f not in folder_names:
            if f.endswith(".mp4") or f.endswith(".wmv") or f.endswith(".mkv") or f.endswith(".mov") or f.endswith(".avi"):
                shutil.move(os.path.join(path, f),path+"\Video")
            elif f.endswith(".mp3") or f.endswith(".wav") :
                shutil.move(os.path.join(path, f),path+"\Audio")
            elif f.endswith(".doc") or f.endswith(".docx") or f.endswith(".odt") or f.endswith(".txt") or f.endswith(".rtf"):  
                shutil.move(os.path.join(path, f),path+"\Text")  
            elif f.endswith(".pdf"):
                shutil.move(os.path.join(path, f),path+"\PDFs")
            elif f.endswith(".zip") or f.endswith(".tar"):
                shutil.move(os.path.join(path, f),path+"\Zips")
            elif f.endswith("exe"):
                shutil.move(os.path.join(path, f),path+"\Executable Files")
            elif f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".gif"):
                shutil.move(os.path.join(path, f),path+"\Images")
            elif "." in f:
                shutil.move(os.path.join(path, f),path+"\Other files")
            else:
                shutil.move(os.path.join(path, f),path+"\Other folders")    
        

#getting path for download folder
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

#creating list of files present in Download folder
files = os.listdir(downloads_path)

create_folders(downloads_path)
print(files[0])
send_files(files,downloads_path)


