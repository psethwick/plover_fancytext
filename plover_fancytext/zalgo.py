from typing import List
from plover.formatting import _Action

import random

from .character_helpers import COMBINING_MARKS
from .formatterbase import FormatterBase


class Zalgo(FormatterBase):

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        assert self.minimum <= self.maximum
        self.reset_state()

    def reset_state(self):
        self.translations = {}

    def add_combining_marks(self, c: str) -> str:
        # In order for suffix folding to work, going to need some determinism
        # otherwise Assert Failed! in formatting.py
        if c in self.translations:
            return self.translations[c]

        for m in random.sample(
                COMBINING_MARKS,
                random.randrange(self.minimum, self.maximum)):
            o = c
            o += m
            self.translations[c] = o
        return o

    def format(self, str) -> str:
        if str:
            return ''.join(self.add_combining_marks(s) for s in str)
        return None

    def process_actions(self, new: List[_Action]):
        for a in new:
            if a.text:
                a.text = (self.format(a.text))
            if a.word:
                a.word = (self.format(a.word))
            if a.prev_replace:
                a.prev_replace = self.format(a.prev_replace)
        # can reset every set of actions
        # the memoization is so that prev_replace won't throw errors
        # if prev_replace isn't at the end of the last action's .text
        self.reset_state()
