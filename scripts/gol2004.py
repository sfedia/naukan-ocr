from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

# from processors.PdfToJpgPages import PdfToJpgPages

# conv = PdfToJpgPages(
#     "/app/data/gol2004-raw/gol2004.pdf",
#     "/app/data/gol2004-pages",
#     "gol2004"
# )
# conv.convert()

from processors.ImagesToBoxes import ImagesToBoxes
from processors.PinModel import PinModel

PinModel("ynk-nenl1985-v3.1", "train/nenl1985/ynk.traineddata", "ynk").pin()
conv = ImagesToBoxes(
    "/app/data/gol2004-pages-clean",
    "/app/data/gol2004-boxes",
    extension="jpg",
    img_name_prefix="gol2004"
)
conv.convert()