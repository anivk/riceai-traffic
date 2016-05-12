from os import listdir
from os.path import isfile, join

mypath = "C:\\flow"
for folder in listdir(mypath):
    if not isfile(join(mypath,folder)):
        folder_path = join(mypath,folder)
        for json_file in listdir(folder_path):
            if json_file.endswith('.json'):
                json_file_path = join(folder_path, json_file)
                with open('script.cmd', 'a') as f:
                    f.write(r'"C:\Program Files\MongoDB\Server\3.2\bin\mongoimport.exe" --host localhost --port 27017 --collection flow --db traffic --file "'+json_file_path+ '" --numInsertionWorkers 16' + '\n')




