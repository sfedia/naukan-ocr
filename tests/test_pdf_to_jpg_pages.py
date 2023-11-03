from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PdfToJpgPages import PdfToJpgPages

conv = PdfToJpgPages(
    "/app/data/nenl1990-raw/nenl1990.pdf",
    "/app/data/test-pages",
    "nenl1990"
)
conv.convert()