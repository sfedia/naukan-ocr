from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PdfToJpgPages import PdfToJpgPages

# conv = PdfToJpgPages(
#     "/app/data/enm2016-raw/enm2016.pdf",
#     "/app/data/enm2016-pages",
#     "enm2016"
# )
# conv.convert()

from processors.ImagesToBoxes import ImagesToBoxes
from processors.PinModel import PinModel

PinModel("ynk-enm2016-v2", "train/enm2016/ynk.traineddata", "ynk").pin()
# conv = ImagesToBoxes(
#     "/app/data/enm2016-pages",
#     "/app/data/enm2016-pages-boxes",
#     extension="jpg",
#     img_name_prefix="ynk.enm2016"
# )
# conv.convert()

# from processors.ImagesToTexts import ImagesToTexts

# ImagesToTexts("/app/data/enm2016-pages", "/app/data/enm2016-texts", extension="jpg", lang="ynk").convert()

# from processors.ImagesToHocrs import ImagesToHocrs
# ImagesToHocrs("/app/data/enm2016-pages", "/app/data/enm2016-hocrs", extension="jpg", lang="ynk").convert()

from processors.RuleBasedTextFormatter import RuleBasedTextFormatter, Token


def format_token(token):
    uppercase_ratio = sum([(1 if char.isupper() else 0) for char in token]) / len(token)
    if uppercase_ratio < 0.8:
        token = "".join([(char if e == 0 else char.lower()) for e, char in enumerate(token)])
    else:
        token = token.upper()
    token = re.sub(r'ьп', 'ыт', token)
    token = re.sub(r'ь1', 'ы', token)
    token = re.sub(r'\.ґ', 'т', token)
    token = re.sub(r'с2', '?', token)
    return token


class FToken(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def format(self):
        self.text = format_token(self.text)


RuleBasedTextFormatter("/app/data/enm2016-texts", "/app/data/enm2016-texts-fmt").format(
    FToken
)

from processors.RuleBasedHocrFormatter import RuleBasedHocrFormatter

class Enm2016_RuleBasedHocrFormatter(RuleBasedHocrFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def process_token(self, token):
        return format_token(token)


Enm2016_RuleBasedHocrFormatter("/app/data/enm2016-hocrs", "/app/data/enm2016-hocrs-fmt").format()

from processors.PagesHocrsMerge import PagesHocrsMerge

merger = PagesHocrsMerge(
    hocr_input_dir="/app/data/enm2016-hocrs-fmt",
    pages_input_dir="/app/data/enm2016-pages",
    output_dir="/app/data/enm2016-hocr-merged"
)
merger.merge()