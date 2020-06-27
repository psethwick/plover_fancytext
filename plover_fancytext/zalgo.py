import random

from .character_helpers import COMBINING_MARKS
from .fancybase import FancyBase


class Zalgo(FancyBase):

    def add_combining_marks(self, c: str) -> str:
        for m in random.sample(COMBINING_MARKS, random.randrange(1, 3)):
            c += m
        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.add_combining_marks(s) for s in str)
        return None
