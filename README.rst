****************************
Fancy Text Plugin for Plover
****************************

This is a plugin for the open source stenography program `Plover <https://www.openstenoproject.org/plover/>`

Requires Plover version 4.0.0 or later

What it does
############


Allows you to use Plover to output text in various (mostly joke, mostly unicode) text formats

Examples:

* bubble:  ⓑⓤⓑⓑⓛⓔ
* medieval:  𝕸𝖊𝖉𝖎𝖊𝖛𝖆𝖑
* fullwidth:  ｖａｐｏｒｗａｖｅ
* sarcasm:  wELl ThIs IS cONvEnIeNt
* upsidedown:  ndsᴉpǝ poʍu
* zalgo:  z̓ä́l̘g̩̚o͡t́èx͓͠ẗ̬

Installing
##########


1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select 'plover_fancytext' in the list
4. Click install
5. Restart Plover
6. In the Configure menu, navigate to the plugins section
7. Enable 'plover_fancytext' and apply

Usage
#####

You'll need to add Plover dictionary entries to toggle on/off the modes

The format is ``{:fancytext_set:<mode>}`` to turn on the mode and simply ``{:fancytext_set}`` to turn off any mode.

Here's what I use (``23*9`` is more easily read as ``#TP*T``):
::

    {
    "23*9": "{#}",
    "23*9/PW-UB": "{:fancytext_set:bubble}",
    "23*9/PH-ED": "{:fancytext_set:medieval}",
    "23*9/TP-UL": "{:fancytext_set:fullwidth}",
    "23*9/SA-RBG": "{:fancytext_set:sarcasm}",
    "23*9/-UP": "{:fancytext_set:upsidedown}",
    "23*9/STKPWA-L": "{:fancytext_set:zalgo}",
    "23*9/23*9": "{:fancytext_set}"
    }

Contributing
############

Want a new mode? Having problems?

Head to the `open source repository <https://github.com/psethwick/plover_fancytext>`

Feel free to:
- Raise an issue
- Open a pull request, new modes accepted!
