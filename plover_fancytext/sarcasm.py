import re


class Sarcasm():

    def __init__(self):
        # TODO these RE's should live in character helpers
        self.consonent_re = \
            re.compile("[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]")

        self.vowel_re = re.compile("[aeiouAEIOU]")
        self.reset_state()

    def reset_state(self):
        self.first_letter = True
        self.capped_last_consonent = False
        self.capped_last = False

    def case_letter(self, c: str) -> str:
        # first letter is a special case
        if self.first_letter:
            if self.vowel_re.match(c):
                self.first_letter = False

            if self.consonent_re.match(c):
                self.first_letter = False
            return c.lower()

        # consonents alternate
        if self.consonent_re.match(c):
            if self.capped_last_consonent:
                self.capped_last_consonent = False
                self.capped_last = False
                return c.lower()

            self.capped_last = True
            self.capped_last_consonent = True
            return c.upper()

        if self.vowel_re.match(c):
            if self.capped_last:
                self.capped_last = False
                return c.lower()
            else:
                self.capped_last = True
                return c.upper()

        if c == '\n':
            self.reset_state()

        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.case_letter(s) for s in str)
        return None


# the first letter must be a lower
# Every second consonent must be upper
# if vowel after a lower it must be upper
# if vowel comes after an upper it must be lower

# assume spaces/punctuation has no effect?
