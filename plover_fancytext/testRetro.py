from unittest import TestCase
from .retro import fancytext_retro

from plover.formatting import _Action


class FakeContext():
    def __init__(self, actions):
        self.actions = actions

    def copy_last_action(self):
        return self.actions[-1]

    def last_words(self, count):
        return [a.word for a in self.actions[-count:]]


class TestRetro(TestCase):

    def test_retro_sarcasm(self):
        action = _Action(word="fancy", text="fancy")
        retroed = fancytext_retro(FakeContext([action]), "1:sarcasm")

        self.assertEqual(retroed.prev_replace, "fancy")
        self.assertEqual(retroed.text, "fANcY")
        self.assertIsNone(retroed.word)
        self.assertTrue(retroed.prev_attach)
