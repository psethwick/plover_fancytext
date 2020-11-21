from typing import List
from threading import Thread

from plover.engine import StenoEngine
from plover import log
from plover.registry import registry
from plover.formatting import _Context, _Action

from .common import TRANSFORMERS


class ExtensionPlugin(Thread):

    def __init__(self, engine: StenoEngine) -> None:
        super().__init__()

        log.info("FANCY_INIT")
        registry.register_plugin('meta', 'fancytext_set', self.fancy_set)

        self.formatter = None
        self.engine = engine
        self.transformers = TRANSFORMERS

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
            self.formatter.process_actions(new)
