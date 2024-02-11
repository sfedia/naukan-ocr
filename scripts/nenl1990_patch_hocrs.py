from os.path import abspath, dirname, join as path_join
import sys
import re
sys.path.append(dirname(abspath(path_join(__file__, ".."))))


# from processors.TextBasedHocrPatcher import TextBasedHocrPatcher

# patcher = TextBasedHocrPatcher(
#     "/app/data/nenl1990-hocrs-2/",
#     "/app/data/nenl1990-pages-corrected/",
#     "/app/data/nenl1990-hocrs-patched/"
# )
# patcher.patch()

from processors.PagesHocrsMerge import PagesHocrsMerge

merger = PagesHocrsMerge(
    hocr_input_dir="/app/data/nenl1990-hocrs-patched",
    pages_input_dir="/app/data/nenl1990-pages-2",
    output_dir="/app/data/nenl1990-hocr-patched-merged"
)
merger.merge()