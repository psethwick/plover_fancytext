import random

from .character_helpers import COMBINING_MARKS


class Zalgo():

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        assert self.minimum <= self.maximum

    def add_combining_marks(self, c: str) -> str:
        for m in random.sample(
                COMBINING_MARKS,
                random.randrange(self.minimum, self.maximum)):
            c += m
        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.add_combining_marks(s) for s in str)
        return None
