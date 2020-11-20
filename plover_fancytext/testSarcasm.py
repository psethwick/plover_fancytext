import unittest
from .sarcasm import Sarcasm

from plover.formatting import _Action


class TestSarcasm(unittest.TestCase):

    def test_input_case(self):
        s = Sarcasm()
        self.assertEqual(s.format("TEST"), "tESt")

    def test_vowels_alternate(self):
        s = Sarcasm()
        self.assertEqual(s.format("eeeeeeee"), "eEeEeEeE")

    def test_consonants_alternate(self):
        s = Sarcasm()
        self.assertEqual(s.format("bbbbbbbb"), "bBbBbBbB")

    def test_whitespace(self):
        s = Sarcasm()
        self.assertEqual(s.format(" test"), " tESt")

    def test_punctuation(self):
        s = Sarcasm()
        self.assertEqual(s.format("(test)"), "(tESt)")

    def test_oh_really(self):
        s = Sarcasm()
        self.assertEqual(s.format("oh really?"), "oH rEaLlY?")

    def test_nice_jacket(self):
        s = Sarcasm()
        self.assertEqual(s.format("nice jacket"), "nICe jACkET")

    def test_look_great(self):
        s = Sarcasm()
        self.assertEqual(s.format("you look great"), "yOu LoOk GrEaT")

    def test_borrow_pencil(self):
        s = Sarcasm()
        self.assertEqual(s.format("can I borrow a pencil?"),
                         "cAN i bORrOW a pENcIL?")

    def test_replace_action(self):
        s = Sarcasm()
        a = [
            _Action(text="previous text"),
            _Action(prev_replace="previous text", text="new text")
        ]
        s.process_actions(a)
        self.assertTrue(a[0].text.endswith(a[1].prev_replace))
