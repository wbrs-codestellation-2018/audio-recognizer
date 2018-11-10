import os
import subprocess
from acrcloud.recognizer import ACRCloudRecognizer

if os.path.isfile('environ.py'):
    exec(open('./environ.py').read() )

config = {
        #Replace "xxxxxxxx" below with your project's host, access_key and access_secret.
        'host': os.environ['ACR_HOST'],
        'access_key': os.environ['ACR_ACCESS_KEY'], 
        'access_secret': os.environ['ACR_ACCESS_SECRET'],
        'timeout':10 # seconds
    }
recognizer = ACRCloudRecognizer(config)
def getGenresFromFile(filename):
    print(recognizer.recognize_by_file(filename))

