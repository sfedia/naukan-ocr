import os
import sys
import subprocess


class ImagesToHocrs:
    def __init__(self, input_dir, output_dir, extension, lang):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.extension = extension
        self.lang = lang

    def convert(self):
        for dirname in (self.input_dir, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        pics = [fn for fn in os.listdir(self.input_dir) if fn.endswith(f".{self.extension}")]
        pics = sorted(pics)
        i = 0
        for picture in pics:
            name, extension = picture.rsplit(".", 1)
            cmd = (
                f'tesseract --oem 0 -l {self.lang} {self.input_dir}/{picture} {self.output_dir}/{name} hocr'
            )
            res = subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(res)
            print(f"Made box for {picture}")
            i += 1
