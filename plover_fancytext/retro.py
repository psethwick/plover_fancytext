from plover.formatting import _Context, _Action

from .common import TRANSFORMERS


def fancytext_retro(ctx: _Context, cmdline: str) -> _Action:
    action = ctx.copy_last_action()
    args = cmdline.split(':')

    # should be <numwords>:mode:<any extra mode args>
    count = int(args.pop(0))
    mode = args.pop(0)

    transformer = TRANSFORMERS[mode](*args)

    last_words = ''.join(ctx.last_words(count=count))

    action.word = None
    action.text = transformer.format(last_words)

    action.prev_replace = last_words
    action.prev_attach = True

    return action
