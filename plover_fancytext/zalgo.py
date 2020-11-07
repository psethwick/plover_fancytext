import random

from .character_helpers import COMBINING_MARKS


class Zalgo():

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        assert self.minimum <= self.maximum
        # In order for suffix folding to work, going to need some determinism
        # otherwise Assert Failed! in formattiny.py
        self.translations = {}

    def add_combining_marks(self, c: str) -> str:
        if c in self.translations:
            return self.translations[c]

        for m in random.sample(
                COMBINING_MARKS,
                random.randrange(self.minimum, self.maximum)):
            o = c
            o += m
            self.translations[c] = o
        return o

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.add_combining_marks(s) for s in str)
        return None
