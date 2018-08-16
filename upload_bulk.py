
from cli import slack
import os
import time


while True:
    try:
        for file in os.listdir("/home/robbie/Dropbox/MIT/temp"):
            print(file)
            slack.files.upload("/home/robbie/Dropbox/MIT/temp/" + file, channels=['DBUSS42MC'])
            time.sleep(2)
    except:
        print("HTTP Error")
        continue



