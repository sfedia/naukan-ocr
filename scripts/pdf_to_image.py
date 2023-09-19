#!/usr/bin/python3

import sys
from pdf2image import convert_from_bytes

"""
Запускать так:
python3 pdf_to_image.py FILE_PATH DEST_FOLDER FILE_PREFIX
"""

dest_folder = sys.argv[2]
file_prefix = sys.argv[3]
images = convert_from_bytes(open(sys.argv[1], "rb").read())
for i in range(len(images)):
    images[i].save(f"{dest_folder}/{file_prefix}.{i + 1}.jpg")
