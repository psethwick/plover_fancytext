from typing import List
from plover.formatting import _Action

from .character_helpers import CONSONANT_RE, VOWEL_RE
from .formatterbase import FormatterBase


class Sarcasm(FormatterBase):

    # the first letter must be a lower
    # Every second consonant must be upper
    # if vowel after a lower it must be upper
    # if vowel comes after an upper it must be lower

    def __init__(self):
        self.reset_state()

    def reset_state(self):
        self.first_letter = True
        self.capped_last_consonant = False
        self.capped_last = False

    def case_letter(self, c: str) -> str:
        # first letter is a special case
        if self.first_letter:
            if VOWEL_RE.match(c):
                self.first_letter = False

            if CONSONANT_RE.match(c):
                self.first_letter = False
            return c.lower()

        # consonants alternate
        if CONSONANT_RE.match(c):
            if self.capped_last_consonant:
                self.capped_last_consonant = False
                self.capped_last = False
                return c.lower()

            self.capped_last = True
            self.capped_last_consonant = True
            return c.upper()

        if VOWEL_RE.match(c):
            if self.capped_last:
                self.capped_last = False
                return c.lower()
            else:
                self.capped_last = True
                return c.upper()

        return c

    def format(self, str) -> str:
        return ''.join(self.case_letter(s) for s in str)

    def process_actions(self, new: List[_Action]):
        for i, a in enumerate(new):
            if a.combo == 'Return':
                self.reset_state()

            if a.text:
                a.text = (self.format(a.text))
            if a.prev_replace:
                a.prev_replace = new[i-1].text[-len(a.prev_replace):]
