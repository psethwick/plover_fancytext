import re
from .fancybase import FancyBase

UWU_SUBSTITUTIONS = {
    "l": "w",
    "r": "w",
    "v": "w",
}

INTENSE_UWU_SUBSTITUTIONS = {
    "u": "uwu",
    ".": " :3"
}


class Uwu(FancyBase):
    def __init__(self, intense: bool):
        self.intense = intense

    def reset_state(self):
        pass

    def uwuify(self, string: str) -> str:
        string = re.sub("([nN])([aeiouAEIOU])", r"\1y\2", string)
        string = string \
            .replace("tute", "tewt") \
            .replace("Hello", "Hewwoooo <3") \
            .replace("yes", "yaww") \
            .replace("no", "nouu")
        return ''.join([self.uwuify_char(char) for char in string])

    def uwuify_char(self, char: str) -> str:
        result = substitute_with_map(UWU_SUBSTITUTIONS, char)
        if self.intense:
            result = substitute_with_map(INTENSE_UWU_SUBSTITUTIONS, result)
        return result

    def __call__(self, string: str) -> str:
        if string:
            return self.uwuify(string)
        return None


def substitute_with_map(substitutions, char: str) -> str:
    result = substitutions.get(char.lower())
    if result is None:
        return char
    elif char.isupper():
        return result.capitalize()
    else:
        return result
