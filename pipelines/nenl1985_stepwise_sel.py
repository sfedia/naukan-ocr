import sys
import os
import subprocess

os.mkdir("./output/nenl1985-additional")

for i in range(8, 43, 2):
    fn = f"./output/nenl1985/page-{str(i).zfill(3)}.txt"
    cmd = f'''
    cp {fn} ./output/nenl1985-additional/;
    '''
    res = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(f"Copied {fn}")