from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.TextBasedHocrPatcher import TextBasedHocrPatcher

patcher = TextBasedHocrPatcher(
    "/app/data/test-enm2016-hocrs/",
    "/app/data/test-enm2016-pages-corrected/",
    "/app/data/test-enm2016-patched-hocrs/"
)
patcher.patch()