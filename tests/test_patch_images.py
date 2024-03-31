from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PatchImages import PatchImages

def patch(imdraw):
    imdraw.rectangle([(1290,0),(1570,90)], fill="white")


conv = PatchImages(
    "/app/data/impatch-test-input",
    "/app/data/impatch-test-output",
)
conv.patch = patch
conv.convert()
