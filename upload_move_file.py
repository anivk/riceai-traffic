__author__ = 'anivk'

from ftplib import FTP
import os
import time

logfile = open('logfile__' + time.strftime("%Y_%m_%d-%H:00h") + '.txt', 'w+')

def file_upload(link, file):
    try:
        link.storbinary("STOR " + file, open(file, 'rb'))

        if link.size(file) is not None:
            logfile.write('\n')
            logfile.write("file_upload -- File successfully uploaded: " + file + "\n")

        os.remove(file)
        logfile.write("remove -- File successfully removed: " + file + "\n")

    except:
        logfile.write("\n\n")
        logfile.write("ERROR! ERROR! ERROR!\nANI AND TIAN LOOK ITS AN ERROR!!!\nERROR! ERROR! ERROR!\n")
        logfile.write("ERROR -- file_upload -- File failed uploading and so it was not removed: " + file+ "\n")
        logfile.write("\n\n")

def run(str_filename):
    server_connection = FTP('ftp.anivk.com')
    server_connection.login('riceai_ani@anivk.com', 'ttt124!@#riceilovetianani')

    file_upload(server_connection, str_filename)

    server_connection.close()

run("Untitled copy 2.rtf")
run("Untitled copy 2.rtf")
run("Untitled copy 2.rtf")
run("Untitled copy 3.rtf")
run("Untitled copy 4.rtf")
run("Untitled copy 5.rtf")
run("Untitled copy 6.rtf")
run("Untitled copy 7.rtf")
run("Untitled copy 8.rtf")
run("Untitled copy 9.rtf")
run("Untitled copy.rtf")