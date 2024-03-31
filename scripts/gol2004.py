from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PdfToJpgPages import PdfToJpgPages

conv = PdfToJpgPages(
    "/app/data/gol2004-raw/gol2004.pdf",
    "/app/data/gol2004-pages",
    "gol2004"
)
conv.convert()