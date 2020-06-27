from .fancybase import FancyBase


class Substitute(FancyBase):

    def __init__(self, character_map, start=None, end=None):
        self._character_map = character_map
        self._start = None
        self._end = None
        if start:
            self._start = start
        if end:
            self._end = end

    def fancy_start(self):
        return self._start

    def fancy_end(self):
        return self._end

    def swap(self, c: str) -> str:
        if c in self._character_map:
            return self._character_map[c]
        return c

    def __call__(self, str: str) -> str:
        if str is None:
            return None
        return ''.join(self.swap(c) for c in str)
