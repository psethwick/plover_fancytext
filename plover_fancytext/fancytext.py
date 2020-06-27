from threading import Thread
from plover.engine import StenoEngine
from plover import log

from plover.registry import registry
from plover.formatting import _Context

from .randomcap import RandomCap
from .zalgo import Zalgo
from .substitute import Substitute
from .character_helpers import BUBBLE_MAP, MEDIEVAL_MAP, UPSIDE_DOWN_MAP
from .character_helpers import DIR_LEFT, DIR_RIGHT


class PloverPlugin(Thread):

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("FANCY_INIT")
        registry.register_plugin('meta', 'fancytext_set', self.fancy_set)

        self.formatter = None
        self.format_start = None
        self.format_end = None
        self.engine = engine
        self.transformers = {
            'bubble': Substitute(BUBBLE_MAP),
            'medieval': Substitute(MEDIEVAL_MAP),
            'randomcap': RandomCap(),
            'upsidedown': Substitute(UPSIDE_DOWN_MAP, DIR_LEFT, DIR_RIGHT),
            'zalgo': Zalgo()
        }

    def fancy_set(self, ctx: _Context, cmdline):
        if cmdline in self.transformers:
            new_formatter = self.transformers[cmdline]
        else:
            new_formatter = None
        old_formatter = self.formatter

        self.formatter = new_formatter
        if new_formatter:
            self.format_start = new_formatter.format_start()
        if old_formatter:
            self.format_end = old_formatter.format_end()
        return ctx.new_action()

    def start(self) -> None:
        log.info("FANCY_START")
        self.engine.hook_connect("translated", self.translated)
        super().start()

    def stop(self) -> None:
        self.engine.hook_disconnect("translated", self.translated)

    def translated(self, old, new):
        if self.formatter:
            if self.format_start:
                pre = self.format_start
                self.format_start = None
            else:
                pre = ''
            if self.format_end:
                post = self.format_end
                self.format_end = None
            else:
                post = ''

            log.info(old)
            log.info(new)

            # probably going to need the index of new
            # if we encounter a prev_replace we need to make sure that:
            # prev_replace and the end of the _previous action_ are the same
            for t in new:
                if t.prev_replace:
                    t.prev_replace = pre + self.formatter(t.prev_replace) + post
                t.word = pre + self.formatter(t.word) + post
                t.text = pre + self.formatter(t.text) + post
