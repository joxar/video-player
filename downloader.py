#!/usr/bin/env python
import os
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('setting.ini')
sec = 'develop'

INFILE = config.get(sec, 'URLS_FILE')
OUTDIR = config.get(sec, 'MP4_DIR')

for url in open(INFILE, 'r'):
    os.chdir(OUTDIR)
    subprocess.call("youtube-dl " + url, shell=True)
