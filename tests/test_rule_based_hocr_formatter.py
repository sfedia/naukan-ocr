from os.path import abspath, dirname, join as path_join
import sys
sys.path.append(dirname(abspath(path_join(__file__, ".."))))

from processors.RuleBasedHocrFormatter import RuleBasedHocrFormatter

class TestRuleBasedHocrFormatter(RuleBasedHocrFormatter):
    def __init__(self, *args, **kwargs):
        RuleBasedHocrFormatter.__init__(self, *args, **kwargs)
    
    def process_token(self, token):
        token = "".join(
            char if e == 0 else (
                char.lower() if char.isupper() else char
            )
            for (e, char) in enumerate(token)
        )

        return token


conv = TestRuleBasedHocrFormatter(
    "/app/data/example-hocr-pairs/",
    "/app/data/example-hocr-pairs/"
)



conv.format()