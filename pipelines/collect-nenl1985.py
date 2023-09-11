import sys
import os
import subprocess

pics = [fn for fn in os.listdir("src/nenl1985") if fn.endswith(".jpg")]
pics = list(sorted(pics, key=lambda fn: int(fn.split(".")[-2])))

i = 1
for picture in pics[1:]:
    cmd = f'''
    cp src/nenl1985/{picture} input/nenl1985/{picture};
    convert "input/nenl1985/{picture}" -crop 900x1100+440+0 "input/nenl1985/page-{str(i).zfill(3)}.jpg";
    convert "input/nenl1985/{picture}" -crop 900x1100+1400+0 "input/nenl1985/page-{str(i + 1).zfill(3)}.jpg";
    rm -f "input/nenl1985/{picture}";
    '''
    res = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(f"{picture} ==> page-{str(i).zfill(3)}, page-{str(i + 1).zfill(3)}")
    i += 1