import unittest
from .sarcasm import Sarcasm


class TestSarcasm(unittest.TestCase):

    def test_input_case(self):
        s = Sarcasm()
        self.assertEqual(s("TEST"), "tESt")

    def test_vowels_alternate(self):
        s = Sarcasm()
        self.assertEqual(s("eeeeeeee"), "eEeEeEeE")

    def test_consonants_alternate(self):
        s = Sarcasm()
        self.assertEqual(s("bbbbbbbb"), "bBbBbBbB")

    def test_whitespace(self):
        s = Sarcasm()
        self.assertEqual(s(" test"), " tESt")

    def test_punctuation(self):
        s = Sarcasm()
        self.assertEqual(s("(test)"), "(tESt)")

    def test_oh_really(self):
        s = Sarcasm()
        self.assertEqual(s("oh really?"), "oH rEaLlY?")

    def test_nice_jacket(self):
        s = Sarcasm()
        self.assertEqual(s("nice jacket"), "nICe jACkET")

    def test_look_great(self):
        s = Sarcasm()
        self.assertEqual(s("you look great"), "yOu LoOk GrEaT")

    def test_borrow_pencil(self):
        s = Sarcasm()
        self.assertEqual(s("can I borrow a pencil?"), "cAN i bORrOW a pENcIL?")
