from .zalgo import Zalgo
from .uwu import Uwu
from .crytyping import CryTyping
from .sarcasm import Sarcasm
from .substitute import Substitute
from .figlet import Figletise
from .character_helpers import \
    BUBBLE_MAP, MEDIEVAL_MAP, UPSIDE_DOWN_MAP, FULLWIDTH_MAP, MORSE_MAP

TRANSFORMERS = {
    'bubble': lambda: Substitute(BUBBLE_MAP),
    'morse': lambda: Substitute(MORSE_MAP, ' '),
    'crytyping': lambda: CryTyping(),
    'medieval': lambda: Substitute(MEDIEVAL_MAP),
    'fullwidth': lambda: Substitute(FULLWIDTH_MAP),
    'uwu': lambda: Uwu(intense=False),
    'UwU': lambda: Uwu(intense=True),
    'sarcasm': lambda: Sarcasm(),
    'figlet': lambda font='slant': Figletise(font),
    'upsidedown': lambda: Substitute(UPSIDE_DOWN_MAP),
    'zalgo': lambda minimum=1, maximum=3: Zalgo(int(minimum),
                                                int(maximum))
}
