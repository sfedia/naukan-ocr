import os
import subprocess
import lxml.html


class RuleBasedHocrFormatter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
    
    def process_token(self, token):
        """Overridable"""
        return token

    def format(self):
        hocr_files = [fn for fn in os.listdir(self.input_dir) if fn.endswith(".hocr")]
        for hocr_fn in hocr_files:
            hocr = lxml.html.fromstring(open(os.path.join(self.input_dir, hocr_fn), "rb").read())
            token_elements = hocr.xpath("//*[@class='ocrx_word']/strong")
            for token_elem in token_elements:
                token_elem.text = self.process_token(token_elem.text)
            with open(os.path.join(self.input_dir, hocr_fn), "w") as file:
                file.write(lxml.html.tostring(hocr, encoding='unicode'))
                file.close()