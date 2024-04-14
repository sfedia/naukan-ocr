from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PdfToJpgPages import PdfToJpgPages

conv = PdfToJpgPages(
    "/app/data/gol2004-raw/gol2004.pdf",
    "/app/data/gol2004-pages-2",
    "gol2004"
)
conv.convert()

from processors.PatchImages import PatchImages

def patch(imdraw):
    imdraw.rectangle([(1265,0),(1590,70)], fill="white")


conv = PatchImages(
    "/app/data/gol2004-pages-2",
    "/app/data/gol2004-pages-clean-2",
)
conv.patch = patch
conv.convert()


from processors.ImagesToBoxes import ImagesToBoxes
from processors.PinModel import PinModel

PinModel("ynk-gol2004-v1", "train/gol2004/ynk.traineddata", "ynk").pin()
conv = ImagesToBoxes(
    "/app/data/gol2004-pages-clean-2",
    "/app/data/gol2004-boxes-3",
    extension="jpg",
    img_name_prefix="ynk.gol2004"
)
conv.convert()

# from processors.ImagesToTexts import ImagesToTexts

# ImagesToTexts("/app/data/gol2004-pages-clean", "/app/data/gol2004-texts", extension="jpg", lang="ynk").convert()

"""Convert using gol2004i model"""
PinModel("ynk-gol2004i-v1", "train/gol2004i/ynk.traineddata", "ynk").pin()
conv = ImagesToBoxes(
    "/app/data/gol2004-pages-clean-2",
    "/app/data/gol2004i-boxes-2",
    extension="jpg",
    img_name_prefix="ynk.gol2004i"
)
conv.convert()

from processors.ImagesToTexts import ImagesToTexts

ImagesToTexts("/app/data/gol2004-pages-clean-2", "/app/data/gol2004i-texts", extension="jpg", lang="ynk").convert()