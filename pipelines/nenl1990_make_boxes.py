import sys
import os
import subprocess

# tesseract --oem 0 -l rus ynk.nenl1985.exp1.jpg ynk.nenl1985.exp1 batch.nochop makebox

os.chdir("input/nenl1990-box-sources")

pics = [fn for fn in os.listdir(".") if fn.endswith(".jpg")]

for picture in pics:
    name, extension = picture.rsplit(".", 1)
    cmd = f'''
    tesseract --oem 0 -l ynk {name}.jpg {name} batch.nochop makebox
    '''
    res = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(res)
    print(f"Made box for {picture}")