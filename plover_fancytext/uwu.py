import re
from .formatterbase import FormatterBase

UWU_SUBSTITUTIONS = {
    "l": "w",
    "r": "w",
    "v": "w",
}

INTENSE_UWU_SUBSTITUTIONS = {
    "u": "uwu",
    ".": " :3"
}


class Uwu(FormatterBase):
    def __init__(self, intense: bool):
        self.intense = intense

    def uwuify(self, string: str) -> str:
        string = re.sub("([nN])([aeiouAEIOU])", r"\1y\2", string)
        string = string \
            .replace("tute", "tewt") \
            .replace("Hello", "Hewwoooo <3") \
            .replace("yes", "yaww") \
            .replace("no", "nouu")
        return ''.join([self.uwuify_char(char) for char in string])

    def uwuify_char(self, char: str) -> str:
        result = self.substitute_with_map(UWU_SUBSTITUTIONS, char)
        if self.intense:
            result = self.substitute_with_map(INTENSE_UWU_SUBSTITUTIONS,
                                              result)

    def substitute_with_map(self, substitutions, char: str) -> str:
        result = substitutions.get(char.lower())
        if result is None:
            return char
        elif char.isupper():
            return result.capitalize()
        else:
            return result

        return result

    def format(self, string: str) -> str:
        if string:
            return self.uwuify(string)
        return None
