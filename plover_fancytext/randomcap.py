import random

from .fancybase import FancyBase


class RandomCap(FancyBase):

    def cap_randomly(self, c: str) -> str:
        if (random.random() > 0.5):
            return c.upper()
        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.cap_randomly(s) for s in str)
        return None
