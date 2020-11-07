from .fancybase import FancyBase


class Substitute(FancyBase):

    def __init__(self, character_map):
        self._character_map = character_map

    def swap(self, c: str) -> str:
        if c in self._character_map:
            return self._character_map[c]
        return c

    def __call__(self, str: str) -> str:
        if str is None:
            return None
        return ''.join(self.swap(c) for c in str)
