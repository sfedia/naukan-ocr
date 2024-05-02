from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))


from processors.PinModel import PinModel

PinModel("ynk-gol2004-v1", "train/gol2004/ynk.traineddata", "ynk").pin()