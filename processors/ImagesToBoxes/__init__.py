import os
import subprocess


class ImagesToBoxes:
    def __init__(self, input_dir, output_dir, extension, img_name_prefix):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.extension = extension
        self.img_name_prefix = img_name_prefix

    def convert(self):
        os.chdir(self.input_dir)
        pics = [fn for fn in os.listdir(self.input_dir) if fn.endswith(f".{self.extension}")]
        pics = sorted(pics)
        i = 0
        for picture in pics:
            name, extension = picture.rsplit(".", 1)
            cmd = (
                f'tesseract --oem 0 -l ynk {name}.jpg {name} batch.nochop makebox '
                f'&& mv {name}.box {self.output_dir}/{self.img_name_prefix}.exp{i}.box'
                f'&& cp {name}.jpg {self.output_dir}/{self.img_name_prefix}.exp{i}.jpg'
            )
            res = subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                shell=True
            )
            print(res)
            print(f"Made box for {picture}")
            i += 1
