import sys
import os
import subprocess

pics = [fn for fn in os.listdir("src/nenl1985") if fn.endswith(".jpg")]
pics = list(sorted(pics, key=lambda fn: int(fn.split(".")[-2])))

output_folder = sys.argv[1]

i = 1
for picture in pics:
    cmd = f'''
    mkdir -p {output_folder} ;
    cp src/nenl1985/{picture} {output_folder}/{picture};
    convert "{output_folder}/{picture}" -crop 900x1100+440+0 "{output_folder}/page-{str(i).zfill(3)}.jpg";
    convert "{output_folder}/{picture}" -crop 900x1100+1400+0 "{output_folder}/page-{str(i + 1).zfill(3)}.jpg";
    rm -f "{output_folder}/{picture}";
    '''
    res = subprocess.check_output(
        cmd,
        stderr=subprocess.STDOUT,
        shell=True
    )
    print(f"{picture} ==> page-{str(i).zfill(3)}, page-{str(i + 1).zfill(3)}")
    i += 2