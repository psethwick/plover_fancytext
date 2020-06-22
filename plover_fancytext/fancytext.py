from threading import Thread
from plover.engine import StenoEngine
from plover import log

from plover.registry import registry
from plover.formatting import _Context

from .randomcap import randomcap
from .zalgo import zalgo

from .substitute import Substitute
from .character_helpers import UPSIDE_DOWN_MAP

# TODO documentation
# TODO owo
# TODO crytyping
# TODO bubble
# TODO medieval
# TODO might want a right->left mark on upside down?


class PloverPlugin(Thread):

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("FANCY_INIT")
        registry.register_plugin('meta', 'fancytext_set', self.fancy_set)

        self._formatter = None
        self._engine = engine
        self._transformers = {
            'randomcap': randomcap,
            'upsidedown': Substitute(UPSIDE_DOWN_MAP),
            'zalgo': zalgo
        }

    def fancy_set(self, ctx: _Context, cmdline):
        if cmdline in self._transformers:
            # to allow toggling
            if self._formatter != self._transformers[cmdline]:
                self._formatter = self._transformers[cmdline]
        else:
            self._formatter = None
        return ctx.new_action()

    def start(self) -> None:
        log.info("FANCY_START")
        self._engine.hook_connect("translated", self.translated)
        super().start()

    def stop(self) -> None:
        self._engine.hook_disconnect("translated", self.translated)

    def translated(self, old, new):
        if self._formatter:
            for t in new:
                t.word = self._formatter(t.word)
                t.text = self._formatter(t.text)
