#!/usr/bin/env python
import os
import subprocess

CURRENTDIR = os.getcwd()
INFILE = CURRENTDIR + "/song.list"
OUTDIR = CURRENTDIR + "/out"

for url in open(INFILE, 'r'):
    os.chdir(OUTDIR)
    subprocess.call("youtube-dl " + url, shell=True)
