import os
import subprocess


class PageSplitter:
    def __init__(self, input_dir, output_dir, width, height, left_mrg1, top_mrg1, left_mrg2, top_mrg2):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.width = width
        self.height = height
        self.left_mrg1 = left_mrg1
        self.top_mrg1 = top_mrg1
        self.left_mrg2 = left_mrg2
        self.top_mrg2 = top_mrg2

    def split(self):
        for dirname in (self.input_dir, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        pics = [fn for fn in os.listdir(self.input_dir) if fn.endswith(".jpg")]
        pics = list(sorted(pics, key=lambda fn: int(fn.split(".")[-2])))
        i = 1
        for picture in pics:
            cmd = f'''
            mkdir -p {self.output_dir} ;
            cp {self.input_dir}/{picture} {self.output_dir}/{picture};
            convert "{self.output_dir}/{picture}" \\\
                -crop {self.width}x{self.height}+{self.left_mrg1}+{self.top_mrg1} \\\
                "{self.output_dir}/page-{str(i).zfill(3)}.jpg";
            convert "{self.output_dir}/{picture}" \\\
                -crop {self.width}x{self.height}+{self.left_mrg2}+{self.top_mrg2} \\\
                "{self.output_dir}/page-{str(i + 1).zfill(3)}.jpg";
            rm -f "{self.output_dir}/{picture}";
            '''
            subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(f"{picture} ==> page-{str(i).zfill(3)}, page-{str(i + 1).zfill(3)}")
            i += 2
