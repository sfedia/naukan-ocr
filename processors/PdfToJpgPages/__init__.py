from pdf2image import convert_from_path
import tempfile
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
        print("Started converting...")
        with tempfile.TemporaryDirectory() as path:
            images = convert_from_path(self.input_path, output_folder=path)
        for i in range(len(images)):
            images[i].save(f"{self.output_dir}/{self.file_prefix}.{i + 1}.jpg")
            print(f"Saved image #{i}")
