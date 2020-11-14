from typing import List
from threading import Thread

from plover.engine import StenoEngine
from plover import log
from plover.registry import registry
from plover.formatting import _Context, _Action

from .zalgo import Zalgo
from .uwu import Uwu
from .crytyping import CryTyping
from .sarcasm import Sarcasm
from .substitute import Substitute
from .character_helpers import \
    BUBBLE_MAP, MEDIEVAL_MAP, UPSIDE_DOWN_MAP, FULLWIDTH_MAP


class PloverPlugin(Thread):

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("FANCY_INIT")
        registry.register_plugin('meta', 'fancytext_set', self.fancy_set)

        self.formatter = None
        self.engine = engine
        self.transformers = {
            'bubble': lambda: Substitute(BUBBLE_MAP),
            'crytyping': lambda: CryTyping(),
            'medieval': lambda: Substitute(MEDIEVAL_MAP),
            'fullwidth': lambda: Substitute(FULLWIDTH_MAP),
            'uwu': lambda: Uwu(False),
            'UwU': lambda: Uwu(True),
            'sarcasm': lambda: Sarcasm(),
            'upsidedown': lambda: Substitute(UPSIDE_DOWN_MAP),
            'zalgo': lambda minimum=1, maximum=3: Zalgo(int(minimum),
                                                        int(maximum))
        }

    def fancy_set(self, ctx: _Context, cmdline) -> _Action:
        args = cmdline.split(':')
        mode = args.pop(0)
        if mode in self.transformers:
            self.formatter = self.transformers[mode](*args)
        else:
            self.formatter = None

        return ctx.new_action()

    def start(self) -> None:
        log.info("FANCY_START")
        self.engine.hook_connect("translated", self.translated)
        super().start()

    def stop(self) -> None:
        self.engine.hook_disconnect("translated", self.translated)

    def translated(self, old: List[_Action], new: List[_Action]) -> None:
        if self.formatter:

            for a in new:
                if a.combo == 'Return':
                    self.formatter.reset_state()

                if a.text:
                    a.text = (self.formatter(a.text))
                if a.word:
                    a.word = (self.formatter(a.word))
                if a.prev_replace:
                    a.prev_replace = self.formatter(a.prev_replace)
