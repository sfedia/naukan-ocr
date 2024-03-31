from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PatchImages import PatchImages

def patch(imdraw):
    imdraw.rectangle([(1265,0),(1590,70)], fill="white")


conv = PatchImages(
    "/app/data/gol2004-pages",
    "/app/data/gol2004-pages-clean",
)
conv.patch = patch
conv.convert()
