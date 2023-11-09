from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.ImagesToHocrs import ImagesToHocrs
from processors.PinModel import PinModel

PinModel("ynk-nenl1990-v6.5", "train/nenl1990/ynk.traineddata", "ynk").pin()
conv = ImagesToHocrs(
    "/app/data/test-pages-spl",
    "/app/data/test-pages-hocrs",
    extension="jpg",
    lang="ynk"
)
conv.convert()