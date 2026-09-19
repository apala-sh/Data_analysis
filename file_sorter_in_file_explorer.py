import os, shutil #shutil allows high level file operations in file explorer
from pathlib import Path

path = r"C:/Users/Apala/Documents/Data_analysis/py_file_sorter_test/"
#the 'r'==> reads it as a raw string instead of interpreting all the 
#backslash and colon stuff

#check if the folder has any files and print em
files = os.listdir(path) #lists all files in the directory
#print(files)

'''
#file types and check if the folder already exists, if not create it 
file_types = ['png', 'jpg', 'xls', 'doc', 'pdf', 'txt']
for i in file_types:
    if not os.path.exists(path + i):
        os.makedirs(path + i)
'''

#get the extensions of all the files in the folder 
file_ext = []
for i in files:
    file_path = Path(i).suffix
    #print(file_path)
    if file_path == '':
        continue
    elif file_path not in file_ext:
        file_ext.append(file_path)

print(file_ext)

#create folders with extension names
for i in file_ext:
    if not os.path.exists(path + i):
        os.makedirs(path + i)

#match file extension to folder names and move the files 

    


        

