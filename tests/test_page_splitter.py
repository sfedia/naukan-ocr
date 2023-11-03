from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PageSplitter import PageSplitter

spl = PageSplitter(
    "/app/data/test-pages",
    "/app/data/test-pages-spl",
    width=900,
    height=1100,
    left_mrg1=440,
    top_mrg1=0,
    left_mrg2=1400,
    top_mrg2=0
)
spl.split()