import os
import subprocess

INDIR = "./out/"

files = os.listdir(INDIR)
for file in files:
    filePath = INDIR + file
    subprocess.call("omxplayer " + filePath, shell=True)
