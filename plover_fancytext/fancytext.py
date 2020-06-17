from threading import Thread
from plover.engine import StenoEngine
from plover import log

from plover.registry import registry
from plover.formatting import _Context

from plover_fancytext.sarcasm import sarcasm
from plover_fancytext.zalgo import zalgo

# TODO documentation
# TODO owo
# TODO crytyping
# TODO upside down text?
# TODO fancy text?
# TODO possibly hook the MODE:RESET?


class PloverPlugin(Thread):
    """TODO write docstring """

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("FANCY_INIT")
        registry.register_plugin('meta', 'fancytext_set', self.meme_set)

        self._formatter = None
        self._engine = engine
        self._transformers = {
            'sarcasm': sarcasm,
            'zalgo': zalgo
        }

    def fancy_set(self, ctx: _Context, cmdline):
        if cmdline in self._transformers:
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
