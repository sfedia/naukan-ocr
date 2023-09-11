import os
import sys
import subprocess

folder = sys.argv[1]
lang = sys.argv[2]

files_in_folder = os.listdir(folder)

for page in files_in_folder:
    new_name = page.rsplit(".", 1)[0]
    prefix, number = new_name.split("-")
    number = number.zfill(3)
    new_name = prefix + "-" + number
    print(f"Processed {page} ==> {new_name}")
    proc = subprocess.check_output(
        f"tesseract {folder}/{page} {folder}/{new_name} -l {lang}",
        stderr=subprocess.STDOUT,
        shell=True
    )
