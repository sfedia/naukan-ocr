import os
import sys
import subprocess
from PIL import Image, ImageDraw


class PatchImages:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
    
    @staticmethod
    def patch(imdraw):
        pass

    def convert(self):
        for dirname in (self.input_dir, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        pics = [fn for fn in os.listdir(self.input_dir)]
        pics = sorted(pics)
        i = 0
        for picture in pics:
            with Image.open(os.path.join(self.input_dir, picture)) as im:
                print("im.size:", im.size)
                draw = ImageDraw.Draw(im)
                self.patch(draw)
                im.save(os.path.join(self.output_dir, picture), "PNG")
            print(f"Patched image #{i}")
            i += 1
