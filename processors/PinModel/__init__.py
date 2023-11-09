import os
import subprocess


class PinModel:
    def __init__(self, tag, path, lang):
        self.tag = tag
        self.path = path
        self.lang = lang

    def pin(self):        
        cmd = (
            f'git show {self.tag}:{self.path} > /usr/share/tesseract-ocr/4.00/tessdata/{self.lang}.traineddata ;'
        )
        res = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            shell=True
        )
        print(res)
