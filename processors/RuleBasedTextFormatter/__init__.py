import os
import subprocess
import sys
import typing as tp
import re
import lxml.html


class Token:
    def __init__(self, text, left_index, right_index, punct_distance):
        self.text = text
        self.left_index = left_index
        self.right_index = right_index
        self.is_first = (self.left_index == 0)
        self.is_last = (self.right_index == 0)
        self.punct_distance = punct_distance
        self.format()
    
    def __repr__(self) -> str:
        return f"{self.text} [{self.left_index}, {self.right_index}]"
    
    def format(self):
        pass
        # self.text = self.text.replace("‘", "'")

    def __str__(self) -> str:
        return self.text


def tokenize_and_format_line(line: str, token_model: Token) -> tp.List[Token]:
    tokens = line.split()
    l = len(tokens)
    result = []
    for (e, tkn) in enumerate(tokens):
        result.append(token_model(tkn, e, l - e - 1))
    return result


def serialize_line(tokens: tp.List[Token]) -> str:
    return " ".join(map(str, tokens))


def endswith_punct(token):
    return re.search(r'[.?!]\s*$', token)


def format_contents(cnt: str, token_model: Token) -> str:
    result = []
    punct_distance = 0
    for line in cnt.splitlines():
        new_line = []
        tokens = line.split()
        l = len(tokens)
        new_line = []
        for (e, tkn) in enumerate(tokens):
            new_line.append(str(token_model(tkn, e, l - e - 1, punct_distance)))
            if endswith_punct(tkn):
                punct_distance = 0
            else:
                punct_distance += 1
        result.append(" ".join(new_line))
    return "\n".join(ln for ln in result if ln)


class RuleBasedTextFormatter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def format(self, token_model: Token):
        for dirname in (self.input_dir, self.output_dir):
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        # os.chdir(self.input_dir)
        files = os.listdir(self.input_dir)
        for fn in files:
            if not fn.endswith(".txt"):
                continue
            contents = open(os.path.join(self.input_dir, fn), "r", encoding="utf-8").read()
            with open(os.path.join(self.output_dir, fn), "w", encoding="utf-8") as formatted:
                formatted.write(format_contents(contents, token_model))
                formatted.close()
            print(f"Formatted {fn}")
