from .character_helpers import CONSONENT_RE, VOWEL_RE


class Sarcasm():

    # the first letter must be a lower
    # Every second consonent must be upper
    # if vowel after a lower it must be upper
    # if vowel comes after an upper it must be lower

    def __init__(self):
        self.reset_state()

    def reset_state(self):
        self.first_letter = True
        self.capped_last_consonent = False
        self.capped_last = False

    def case_letter(self, c: str) -> str:
        # first letter is a special case
        if self.first_letter:
            if VOWEL_RE.match(c):
                self.first_letter = False

            if CONSONENT_RE.match(c):
                self.first_letter = False
            return c.lower()

        # consonents alternate
        if CONSONENT_RE.match(c):
            if self.capped_last_consonent:
                self.capped_last_consonent = False
                self.capped_last = False
                return c.lower()

            self.capped_last = True
            self.capped_last_consonent = True
            return c.upper()

        if VOWEL_RE.match(c):
            if self.capped_last:
                self.capped_last = False
                return c.lower()
            else:
                self.capped_last = True
                return c.upper()

        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.case_letter(s) for s in str)
        return None
