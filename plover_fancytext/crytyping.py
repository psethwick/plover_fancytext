from typing import List
import random

from .formatterbase import FormatterBase
from .character_helpers import LETTERS

from plover.formatting import _Action


class CryTyping(FormatterBase):

    # swapping two letters
    # adding a random letter
    # doubling a letter
    # adding random punctuation
    # deleting a letter
    # swapping the case of a letter (e.g. a ⇔ A)

    def __init__(self):
        self.reset_state()

    def reset_state(self):
        self.letter_swap = None

    def letter_operations(self, c: str) -> str:
        o = c

        if self.letter_swap:
            o += self.letter_swap
            self.reset_state()
            return o

        if random.randint(1, 100) > 98:
            # delete :D
            return ''

        upper_case_chance = random.randint(1, 100)

        if upper_case_chance > 97:
            o = o.upper()

        swap_chance = random.randint(1, 100)

        if swap_chance > 96:
            self.letter_swap = c
            return ''

        dupe_chance = random.randint(1, 100)
        if dupe_chance > 90:
            o += c

        punc_chance = random.randint(1, 100)
        punc_amount = random.randint(2, 4)

        if punc_chance > 95:
            p = random.choice([',', '.', ';'])
            for x in range(1, punc_amount):
                o += p

        add_random_chance = random.randint(1, 100)

        if add_random_chance > 98:
            o += random.choice(LETTERS)
        return o

    def format(self, str) -> str:
        if str:
            letters = (self.letter_operations(c)
                       for c in str)
            self.reset_state()  # it's ok if we lose a letter
            return ''.join(letters)
        return None

    def process_actions(self, new: List[_Action]):
        for a in new:
            if a.text:
                a.text = (self.format(a.text))
            if a.word:
                a.word = (self.format(a.word))
            if a.prev_replace:
                # if this doesn't match the end of the previous action
                # then plover will throw assertion errors
                # galaxy brain: just get rid of it
                a.prev_replace = None
