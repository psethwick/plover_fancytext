import unittest
import inspect

from plover.formatting import _Action

from .extensionplugin import ExtensionPlugin


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


class TestExtensionPlugin(unittest.TestCase):

    def test_connect_hook(self):
        e = FakeEngine()
        f = ExtensionPlugin(e)
        f.start()
        self.assertIsNotNone(e.method_calls["translated"])

    def test_hook_signature(self):
        e = FakeEngine()
        f = ExtensionPlugin(e)
        f.start()
        hooked_method = e.method_calls["translated"]
        signature = inspect.signature(hooked_method)

        self.assertEqual(len(signature.parameters), 2)
        self.assertIsNotNone(signature.parameters["old"])
        self.assertIsNotNone(signature.parameters["new"])

    def test_disconnect_hook(self):
        e = FakeEngine()
        f = ExtensionPlugin(e)
        f.start()
        f.stop()
        self.assertIsNone(e.method_calls["translated"])

    def test_translate_does_nothing_if_fancy_not_set(self):
        p = self._set_up_plugin()
        old = []
        old.append(self._get_action_return("things"))
        new = []
        new.append(self._get_action_return("stuff"))

        p.translated(old, new)

        self.assertEqual(len(old), 1)
        self.assertEqual(old[0], self._get_action_return("things"))
        self.assertEqual(len(new), 1)
        self.assertEqual(new[0], self._get_action_return("stuff"))

    def test_plugged_bubble(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "bubble")
        new = self._get_action_return("text")
        p.translated([], new)

        self.assertEqual(new[0].text, "ⓣⓔⓧⓣ")

        new = self._get_orthography_thing()
        p.translated([], new)
        self.assertTrue(new[0].text.endswith(new[1].prev_replace))

    def test_plugged_crytyping(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "crytyping")
        # this test .. uh makes sure it doesn't blow up?
        p.translated([], self._get_action_return("text"))
        new = self._get_orthography_thing()
        p.translated([], new)

        # crytyping is too random for prev_replace to work
        self.assertIsNone(new[1].prev_replace)

    def test_plugged_medieval(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "medieval")
        new = self._get_action_return("F")
        p.translated([], new)

        self.assertEqual(new[0].text, "𝕱")

    def test_plugged_fullwidth(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "fullwidth")
        new = self._get_action_return("F")
        p.translated([], new)

        self.assertEqual(new[0].text, "\uFF26")

    def test_plugged_uwu(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "uwu")
        new = self._get_action_return("McNugget")
        p.translated([], new)

        self.assertEqual(new[0].text, "McNyugget")

    def test_plugged_uwu_intense(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "UwU")
        new = self._get_action_return(".")
        p.translated([], new)

        self.assertEqual(new[0].text, " :3")

    def test_plugged_sarcasm(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "sarcasm")
        new = self._get_action_return("testing")
        p.translated([], new)

        self.assertEqual(new[0].text, "tEStINg")

    def test_plugged_upsidedown(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "upsidedown")
        new = self._get_action_return("test")
        p.translated([], new)

        self.assertEqual(new[0].text, "\u0287\u01DD\u0073\u0287")

    def test_plugged_zalgo(self):
        p = self._set_up_plugin()
        p.fancy_set(FakeContext(), "zalgo")
        new = self._get_orthography_thing()
        p.translated([], new)

        self.assertTrue(new[0].text.endswith(new[1].prev_replace))

    def _set_up_plugin(self) -> ExtensionPlugin:
        e = FakeEngine()
        p = ExtensionPlugin(e)
        p.start()
        return p

    def _get_action_return(self, str):
        return [
            _Action(text=str, word=str),
            _Action(combo="Return")
        ]

    def _get_orthography_thing(self):
        return [
            _Action(text="the", word="the"),
            _Action(text="ing", word="thing", prev_replace="e")
        ]
