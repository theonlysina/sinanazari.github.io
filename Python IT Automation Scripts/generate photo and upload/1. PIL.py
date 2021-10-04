#!/usr/bin/env python3

from  PIL import Image
import os

path = "{}{}".format(os.getcwd(),"/supplier-data/images")
for file in os.listdir(path):
        f, e = os.path.splitext(file)
        try:
                im = Image.open(path + "/" + file)
                try:
                        new_im = im.resize((600,400)).convert("RGB")
                        new_im.save("{}/{}.{}".format(path, f, "jpeg"))
                except OSError:
                        print("cannot convert", file)
        except OSError:
                print("cannot open", file)

