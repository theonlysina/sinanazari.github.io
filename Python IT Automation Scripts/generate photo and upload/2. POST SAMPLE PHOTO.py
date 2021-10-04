#!/usr/bin/env python3
import requests
import os

cwd = os.getcwd()
path = "{}/{}".format(cwd, "supplier-data/images")

url = "http://localhost/upload/"
for file in os.listdir(path):
        f, e = os.path.splitext(file)
        print("file: " + f + "." + e)
        if e == ".jpeg":
                with open("{}/{}".format(path, file), 'rb') as opened:
                        r = requests.post(url, files={'file': opened})