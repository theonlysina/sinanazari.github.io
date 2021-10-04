#!/usr/bin/env python3
import requests
import os

cwd = os.getcwd()
path = "{}/{}".format(cwd, "supplier-data/descriptions")
list = []
url = "http://127.0.0.1/fruits/"

for file in os.listdir(path):
        dict = {}
        f, e = os.path.splitext(file)
        with open("{}/{}".format(path, file)) as fruit_file:
                name = dict["name"] = fruit_file.readline().strip()
                dict["weight"] = int(fruit_file.readline().split(" ")[0])
                dict["description"] = fruit_file.readline().strip()
                dict["image_name"] = "{}.jpeg".format(f)
        print(dict)
        list.append(dict)

print(list)

for item in list:
        resp = requests.post(url, json=item)
        if resp.status_code != 201:
                raise Exception('POST error status={}'.format(resp.status_code))
        print('Created feedback ID: {}'.format(resp.json()["id"]))
