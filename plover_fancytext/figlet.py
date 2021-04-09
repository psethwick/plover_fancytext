from typing import List
from plover.formatting import _Action

from .formatterbase import FormatterBase

from pyfiglet import Figlet


class Figletise(FormatterBase):

    def __init__(self, font):
        self.fig = Figlet(font)

    def format(self, str) -> str:
        if str:
            return self.fig.renderText(str)
        return None

    def process_actions(self, new: List[_Action]):
        raise Exception(
            "Mode not supported, use fancy_text_retro:<count>:figlet:<font>"
        )
