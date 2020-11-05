import random

from .character_helpers import LETTERS


class CryTyping():

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

    def __call__(self, str) -> str:
        if str:
            letters = (self.letter_operations(c)
                       for c in str)
            self.reset_state()  # it's ok if we lose a letter
            return ''.join(letters)
        return None
