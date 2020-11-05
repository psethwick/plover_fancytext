import unittest

from .zalgo import Zalgo


class TestZalgo(unittest.TestCase):

    def test_original_included(self):
        z = Zalgo(5, 10)
        zalgo = ["z", "a", "l", "g", "o"]
        output = z("".join(zalgo))

        for c in zalgo:
            self.assertIn(c, output)
