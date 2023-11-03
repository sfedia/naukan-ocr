import subprocess
import os
import re


IMAGE_EXTENSIONS = ("jpg", "jpeg", "png")


class PagesHocrsMerge:
    def __init__(self, hocr_input_dir, pages_input_dir, output_dir):
        self.hocr_input_dir = hocr_input_dir
        self.pages_input_dir = pages_input_dir
        self.output_dir = output_dir

    def get_hocr_files(self):
        hocrs = {}
        for fn in os.listdir(self.hocr_input_dir):
            if not fn.endswith(".hocr"):
                continue

            name, ext = fn.rsplit(".", 1)
            hocrs[name] = os.path.join(self.hocr_input_dir, fn)
        return hocrs
    
    def get_page_files(self):
        pages = {}
        for fn in os.listdir(self.pages_input_dir):
            ok = False
            for ext in IMAGE_EXTENSIONS:
                if fn.endswith("." + ext):
                    ok = True
            if not ok:
                continue

            name, ext = fn.rsplit(".", 1)
            pages[name] = os.path.join(self.pages_input_dir, fn)
        return pages

    def create_output_path(self, name):
        return os.path.join(self.output_dir, name + ".pdf")
    
    def combine_paths(self):
        hocr_files = self.get_hocr_files()
        page_files = self.get_page_files()
        return [(hocr_files[k], page_files[k], self.create_output_path(k)) for k in hocr_files]
    
    def merge(self):
        paths = self.combine_paths()
        subprocess.check_output(
            "cd /app/processors/PagesHocrsMerge/ && npm install --save-dev",
            stderr=subprocess.STDOUT,
            shell=True
        )
        for pth in paths:
            command = "cd /app/processors/PagesHocrsMerge/ && node merge.js " + " ".join(pth)
            print(command)
            subprocess.check_output(
                command,
                stderr=subprocess.STDOUT,
                shell=True
            )
    



