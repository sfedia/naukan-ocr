import sys
import os
import subprocess


# convert exp6.jpg -level 5%,95%,0.2 exp6-2.jpg


working_dir = sys.argv[1]
os.chdir(working_dir)
pics = [fn for fn in os.listdir(".") if fn.endswith(".jpg")]


for picture in pics:
    name, extension = picture.rsplit(".", 1)
    cmd = f'''
    convert {picture} -level 5%,95%,0.2 {picture}
    '''
    res = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(f"Adjusted contrast {picture}")