from os.path import abspath, dirname, join as path_join
import sys
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

PinModel("ynk-enm2016-v1", "train/enm2016/ynk.traineddata", "ynk").pin()
# conv = ImagesToBoxes(
#     "/app/data/enm2016-pages",
#     "/app/data/enm2016-pages-boxes",
#     extension="jpg",
#     img_name_prefix="ynk.enm2016"
# )
# conv.convert()

from processors.ImagesToTexts import ImagesToTexts

ImagesToTexts("/app/data/enm2016-pages", "/app/data/enm2016-texts", extension="jpg", lang="ynk").convert()