import os
import subprocess
import sys
import typing as tp
import re
import lxml.html


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
        pass
        # self.text = self.text.replace("‘", "'")

    def __str__(self) -> str:
        return self.text


def tokenize_and_format_line(line: str, token_model: Token) -> tp.List[Token]:
    tokens = line.split()
    l = len(tokens)
    t = [token_model(tkn, e, l - e - 1) for (e, tkn) in enumerate(tokens)]
    return t


def serialize_line(tokens: tp.List[Token]) -> str:
    return " ".join(map(str, tokens))


def format_contents(cnt: str, token_model: Token) -> str:
    result = []
    for line in cnt.splitlines():
        result.append(serialize_line(tokenize_and_format_line(line, token_model)))
    return "\n".join(ln for ln in result if ln)


class RuleBasedTextFormatter:
    def __init__(self, input_dir):
        self.input_dir = input_dir

    def format(self, token_model: Token):
        os.chdir(self.input_dir)
        files = os.listdir(".")
        for fn in files:
            if not fn.endswith(".txt"):
                continue
            contents = open(fn, "r", encoding="utf-8").read()
            with open(fn, "w", encoding="utf-8") as formatted:
                formatted.write(format_contents(contents, token_model))
                formatted.close()
            print(f"Formatted {fn}")
