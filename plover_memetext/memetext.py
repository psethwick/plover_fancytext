from threading import Event, Thread
from plover.engine import StenoEngine
from plover import log

from plover.registry import registry
from plover.formatting import _Context

# TODO documentation
# TODO ZALGO
# TODO crytyping
# TODO possibly hook the MODE:RESET?


class MemeText(Thread):
    """TODO write docstring """

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("MEME_INIT")
        self._engine = engine
        self._stop_event = Event()
        self._active_modes = []
        self._sarcasm = False

    # TODO: generalise memes, apply many
    def meme_start(self, ctx: _Context, args):
        self._sarcasm = True
        return ctx.new_action()

    def meme_stop(self, ctx: _Context, args):
        self._sarcasm = False
        return ctx.new_action()

    def start(self) -> None:
        log.info("MEME_START")
        registry.register_plugin('meta', 'memetext_start', self.meme_start)
        registry.register_plugin('meta', 'memetext_stop', self.meme_stop)
        self._engine.hook_connect("translated", self.translated)
        super().start()

    def stop(self) -> None:
        self._engine.hook_disconnect("translated", self.translated)
        self._stop_event.set()

    def cap_if_even(self, c, i):
        if i % 2 == 0:
            return c.upper()
        return c

    def sarcasm(self, str) -> str:
        # TODO: make this sarcasm mode for _real_ ugh
        if str:
            return ''.join(self.cap_if_even(s, i) for i, s in enumerate(str))
        return None

    def translated(self, old, new):
        # TODO is there a cleaner way of transforming? this feels clunky
        for t in new:
            if t.word == 'sarcasm':
                self._sarcasm = True
            if self._sarcasm:
                t.word = self.sarcasm(t.word)
                t.text = self.sarcasm(t.text)
