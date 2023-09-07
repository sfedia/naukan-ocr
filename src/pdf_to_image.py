#!/usr/bin/python3

import sys
from pdf2image import convert_from_bytes

"""
Запускать так:
python3 pdf_to_image.py FILE_PATH DEST_FOLDER
"""

dest_folder = sys.argv[2]
images = convert_from_bytes(open(sys.argv[1], "rb").read())
for i in range(len(images)):
    images[i].save(f"{dest_folder}/{dest_folder}.{i + 1}.jpg")
