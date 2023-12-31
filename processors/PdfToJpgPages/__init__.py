from pdf2image import convert_from_bytes
import os

class PdfToJpgPages:
    def __init__(self, input_path, output_dir, file_prefix):
        self.input_path = input_path
        self.output_dir = output_dir
        self.file_prefix = file_prefix

    def convert(self):
        for dirname in (self.input_path, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        images = convert_from_bytes(open(self.input_path, "rb").read())
        for i in range(len(images)):
            images[i].save(f"{self.output_dir}/{self.file_prefix}.{i + 1}.jpg")
