import os
import sys
import typing as tp
import re
import formatter

VOWELS_REGEX = r'[уеыаоэяиюа̀ėёи́Ўў]'
NON_VOWELS_REGEX = r'[^уеыаоэяиюа̀ėёи́Ўў]'

# python3 scripts/nenl1990_format_pages.py

class _Token(formatter.Token):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def format(self):
        self.text = re.sub(fr'({NON_VOWELS_REGEX})[вп]({NON_VOWELS_REGEX})', r'\g<1>а\g<2>', self.text)
        self.text = re.sub(fr'({NON_VOWELS_REGEX})[вп]$', r'\g<1>а', self.text)
        self.text = re.sub(fr'^[вп]({NON_VOWELS_REGEX})', r'а\g<1>', self.text)

        self.text = re.sub(fr'({VOWELS_REGEX})и', r'\g<1>н', self.text)

        self.text = re.sub(fr'({NON_VOWELS_REGEX})н({NON_VOWELS_REGEX})', r'\g<1>и\g<2>', self.text)
        self.text = re.sub(fr'({NON_VOWELS_REGEX})н$', r'\g<1>и', self.text)
        self.text = re.sub(fr'^н({NON_VOWELS_REGEX})', r'и\g<1>', self.text)


formatter.format_files("output/nenl1990", _Token)
