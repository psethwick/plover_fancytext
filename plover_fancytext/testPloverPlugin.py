import unittest
import inspect

from plover.formatting import _Action, _Context

from .fancytext import PloverPlugin


class FakeContext():

    def new_action(self):
        pass


class FakeEngine():

    def __init__(self):
        self.method_calls = {}

    def hook_connect(self, hook: str, method):
        self.method_calls[hook] = method

    def hook_disconnect(self, hook: str, method):
        self.method_calls[hook] = None


class TestPloverPlugin(unittest.TestCase):

    def test_connect_hook(self):
        e = FakeEngine()
        f = PloverPlugin(e)
        f.start()
        self.assertIsNotNone(e.method_calls["translated"])

    def test_hook_signature(self):
        e = FakeEngine()
        f = PloverPlugin(e)
        f.start()
        hooked_method = e.method_calls["translated"]
        signature = inspect.signature(hooked_method)

        self.assertEqual(len(signature.parameters), 2)
        self.assertIsNotNone(signature.parameters["old"])
        self.assertIsNotNone(signature.parameters["new"])

    def test_disconnect_hook(self):
        e = FakeEngine()
        f = PloverPlugin(e)
        f.start()
        f.stop()
        self.assertIsNone(e.method_calls["translated"])

    def test_translate_does_nothing_if_fancy_not_set(self):
        p = self._set_up_plugin()
        old = []
        old.append(self._get_action())
        new = []
        new.append(self._get_action())

        p.translated(old, new)

        self.assertEqual(len(old), 1)
        self.assertEqual(old[0], self._get_action())
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0], self._get_action())

    def test_plugged_sarc(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "sarcasm")
        old = []
        new = []
        new.append(self._get_action())
        new.append(self._get_return_action())
        p.translated(old, new)

        self.assertEqual(new[0].text, "tEXt")

    def test_plugged_bubble(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "bubble")
        old = []
        new = []
        new.append(self._get_action())
        new.append(self._get_return_action())
        p.translated(old, new)

        self.assertEqual(new[0].text, "ⓣⓔⓧⓣ")

    # TODO more plugged tests

    def _set_up_plugin(self) -> PloverPlugin:
        e = FakeEngine()
        p = PloverPlugin(e)
        p.start()
        return p

    def _get_action(self):
        return _Action(text="text", word="text", prev_replace="")

    def _get_return_action(self):
        return _Action(combo="Return")
