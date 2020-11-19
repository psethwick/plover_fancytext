from typing import List
from plover.formatting import _Action


class FormatterBase():

    # default no-state reset
    def reset_state(self):
        pass

    # decent default implementation of processing actions
    # stateful formatters may want to do something different
    # or may not
    def process_actions(self, new: List[_Action]):
        for a in new:
            if a.combo == 'Return':
                self.reset_state()

            if a.text:
                a.text = (self.format(a.text))
            if a.word:
                a.word = (self.format(a.word))
            if a.prev_replace:
                a.prev_replace = self.format(a.prev_replace)
