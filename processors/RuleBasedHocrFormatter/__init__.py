import os
import subprocess
import lxml.html
import re


class RuleBasedHocrFormatter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
    
    def process_token(self, token, internal_index, line_index, punct_distance):
        """Overridable"""
        return token
    
    def endswith_punct(self, token):
        return re.search(r'[.?!]\s*$', token)

    def format(self):
        for dirname in (self.input_dir, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        hocr_files = [fn for fn in os.listdir(self.input_dir) if fn.endswith(".hocr")]
        for hocr_fn in hocr_files:
            hocr = lxml.html.fromstring(open(os.path.join(self.input_dir, hocr_fn), "rb").read())
            line_elements = hocr.xpath("//*[@class='ocr_line']")
            punct_distance = 0
            for j, line_elem in enumerate(line_elements):
                token_elements = line_elem.xpath(".//*[@class='ocrx_word']/strong")
                for e, token_elem in enumerate(token_elements):
                    token_elem.text = self.process_token(token_elem.text, e, j, punct_distance)
                    if self.endswith_punct(token_elem.text):
                        punct_distance = 0
                    else:
                        punct_distance += 1
            with open(os.path.join(self.output_dir, hocr_fn), "w") as file:
                file.write(lxml.html.tostring(hocr, encoding='unicode'))
                file.close()