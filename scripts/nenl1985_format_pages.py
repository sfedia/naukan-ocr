import os
import sys
import typing as tp
import re

folder = sys.argv[1]

os.chdir(folder)

files = os.listdir(".")

class Token:
    def __init__(self, text, left_index, right_index):
        self.text = text
        self.left_index = left_index
        self.right_index = right_index
        self.is_first = (self.left_index == 0)
        self.is_last = (self.right_index == 0)
        self.format()
    
    def __repr__(self) -> str:
        return f"{self.text} [{self.left_index}, {self.right_index}]"
    
    def format(self):
        self.text = self.text.replace("’", "'")
        self.text = self.text.replace("‘", "'")
        if self.is_last:
            self.text = re.sub(r"'$", ",", self.text)
        self.text = re.sub(r'[.](?!$|[.])', '', self.text)
        self.text = re.sub(r'[,](?!$|[,])', '', self.text)
        uc = len([x for x in self.text if x.isupper()])
        lc = len([x for x in self.text if x.islower()])
        if uc >= 2 and lc > 0:
            self.text = self.text.lower()
        if self.is_first:
            self.text = self.text[0].upper() + self.text[1:]

    def __str__(self) -> str:
        return self.text


def tokenize_and_format_line(line: str) -> tp.List[Token]:
    tokens = line.split()
    l = len(tokens)
    t = [Token(tkn, e, l - e - 1) for (e, tkn) in enumerate(tokens)]
    return t


def serialize_line(tokens: tp.List[Token]) -> str:
    return " ".join(map(str, tokens))


def format_contents(cnt: str) -> str:
    result = []
    for line in cnt.splitlines():
        result.append(serialize_line(tokenize_and_format_line(line)))
    return "\n".join(result)


for fn in files:
    if not fn.endswith(".txt"):
        continue
    contents = open(fn, "r", encoding="utf-8").read()
    with open(fn, "w", encoding="utf-8") as formatted:
        formatted.write(format_contents(contents))
        formatted.close()
    print(f"Formatted {fn}")

