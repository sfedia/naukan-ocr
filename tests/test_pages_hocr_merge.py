from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.PagesHocrsMerge import PagesHocrsMerge

merger = PagesHocrsMerge("/app/data/example-hocr-pairs","/app/data/example-hocr-pairs","/app/data/example-hocr-pairs")
merger.merge()