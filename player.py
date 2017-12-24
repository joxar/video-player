import os
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('setting.ini')
sec = 'develop'

INPUT_DIR = config.get(sec, 'MP4_DIR')
files = os.listdir(INPUT_DIR)
for file in files:
    filePath = INPUT_DIR + file
    subprocess.call("omxplayer " + filePath, shell=True)
