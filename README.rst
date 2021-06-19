****************************
Fancy Text Plugin for Plover
****************************

This is a plugin for the open source stenography program `Plover <https://www.openstenoproject.org/plover/>`_

Requires Plover version 4.0.0 or later

.. image:: https://github.com/psethwick/plover_fancytext/workflows/Tests/badge.svg
    :target: https://github.com/psethwick/plover_fancytext/actions?query=workflow%3ATests
.. image:: https://img.shields.io/pypi/v/plover_fancytext.svg
    :target: https://pypi.org/project/plover-fancytext/
.. image:: https://img.shields.io/pypi/dm/plover_fancytext.svg
    :target: https://pypi.org/project/plover-fancytext/

What it does
############


Allows you to use Plover to write *fancy* text

Transformers:

* blackboardbold: 𝔹𝕝𝕒𝕔𝕜𝕓𝕠𝕒𝕣𝕕 𝔹𝕠𝕝𝕕, 𝕒𝕜𝕒 𝔻𝕠𝕦𝕓𝕝𝕖 𝕊𝕥𝕣𝕦𝕔𝕜
* bubble:  ⓑⓤⓑⓑⓛⓔ
* crytyping:   I' finne,,, h ddon'nt w,,,orry about me, re,,el yy
* fullwidth:  ｖａｐｏｒｗａｖｅ
* medieval:  𝕸𝖊𝖉𝖎𝖊𝖛𝖆𝖑
* morse: ... --- ...
* sarcasm:  wELl ThIs IS cONvEnIeNt
* script: 𝓢𝓬𝓻𝓲𝓹𝓽 𝓯𝓸𝓻 𝓽𝓱𝓪𝓽 𝓱𝓪𝓷𝓭𝔀𝓻𝓲𝓽𝓽𝓮𝓷 𝓵𝓸𝓸𝓴
* smallcaps: Sᴍᴀʟʟ Cᴀᴘs
* upsidedown:  ndsᴉpǝ poʍu
* uwu:  Hewwoooo <3 this aww you nyeed.
* UwU:  uwuwuwu, buwut mowe :3 Nyote that this may get in the way of conwewsations :3 :3 :3
* zalgo:  z̓ä́l̘g̩̚o͡t́èx͓͠ẗ̬
* figlet: 

::

    MMMMMMMM               MMMMMMMM                                  
    M:::::::M             M:::::::M                                  
    M::::::::M           M::::::::M                                  
    M:::::::::M         M:::::::::M                                  
    M::::::::::M       M::::::::::M   ooooooooooo      ooooooooooo   
    M:::::::::::M     M:::::::::::M oo:::::::::::oo  oo:::::::::::oo 
    M:::::::M::::M   M::::M:::::::Mo:::::::::::::::oo:::::::::::::::o
    M::::::M M::::M M::::M M::::::Mo:::::ooooo:::::oo:::::ooooo:::::o
    M::::::M  M::::M::::M  M::::::Mo::::o     o::::oo::::o     o::::o
    M::::::M   M:::::::M   M::::::Mo::::o     o::::oo::::o     o::::o
    M::::::M    M:::::M    M::::::Mo::::o     o::::oo::::o     o::::o
    M::::::M     MMMMM     M::::::Mo::::o     o::::oo::::o     o::::o
    M::::::M               M::::::Mo:::::ooooo:::::oo:::::ooooo:::::o
    M::::::M               M::::::Mo:::::::::::::::oo:::::::::::::::o
    M::::::M               M::::::M oo:::::::::::oo  oo:::::::::::oo 
    MMMMMMMM               MMMMMMMM   ooooooooooo      ooooooooooo   

Installing
##########


1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select 'plover_fancytext' in the list
4. Click install
5. Restart Plover
6. If you just want the retro commands, you're done!


Extra steps for the extension plugin (which enables the
``{:fancytext_set:<transformer>}`` commands):

1. In the Configure menu, navigate to the plugins section
2. Enable 'plover_fancytext' and apply

Usage
#####

You can either apply transformations with
``{:fancytext_retro:<number of words>:<transformer>}``
which will replace ``<number of words>`` retroactively with fancy text. Example:
``{:fancytext_retro:2:bubble}`` to bubble-ize the last two words.

Or you can use ``{:fancytext_set:<transformer>}`` to turn on
a mode until you turn it back off!

The format is ``{:fancytext_set:<mode>}`` to turn on the mode and simply ``{:fancytext_set:off}`` to turn off any mode.

Here's what I use (``23*9`` is more easily read as ``#TP*T``):
::

    {
    "23*9": "{:fancytext_set:off}",
    "23*9/PW-UB": "{:fancytext_set:bubble}",
    "23*9/KRAO-EU": "{:fancytext_set:crytyping}",
    "23*9/SRA-EUP": "{:fancytext_set:fullwidth}",
    "23*9/PH-ED": "{:fancytext_set:medieval}",
    "23*9/SA-RBG": "{:fancytext_set:sarcasm}",
    "23*9/-UP": "{:fancytext_set:upsidedown}",
    "23*9/AO-U": "{:fancytext_set:uwu}",
    "23*9/AO*U": "{:fancytext_set:UwU}",
    "23*9/STKPWA-L": "{:fancytext_set:zalgo}"
    }

Mode Notes
##########

It's worth noting that these modes will not always work with Plover's
orthography rules. Some modes will be more wrong than others

The  z̶͉a̕l̬ḡ͙o̕ m͏̎o̬̪d̜e̝̹ can also take two arguments for the minimum and maximum number
of combining marks. Example ``{:fancytext_set:zalgo:10:15}`` for quite a lot of
z͙͕̹̩̀͑ͮ̇̉ͣ̄͋̕ȃ̵̝͎̘̬͙̖̼͆ͤ̕͝ͅ l̵̤̟̜͎͍̠̭̽̿͂ͬͩ͜ģ̲͈͍̔ͩ̀ͣͬ̉ͨ̕̚͝o̴̢̓̓ͦ̈́̂̆͛ͭͣ. For reference the default is min=1, max=3

You may want the 　ｆｕｌｌ　ｗｉｄｔｈ　mode to use a full-width space. This can be done by
setting space in the same entry: ``{:fancytext_set:fullwidth}{MODE:SET_SPACE:　}``.
If you do this you'll probably also want to add ``{MODE:RESET}`` to your entry which turns
off the mode

This trick can also be applied to the upside down mode.
Include unicode 202e (right to left mark) as well as a space character for um, a
good time. You'll definitely want ``{MODE:RESET}`` on this one, and you might want
to add unicode 202d (left to right mark) to it as well. You don't want to use
these marks anywhere where text needs to be precisely correct, but should be
fine in many places. I've not included it as part of the mode because it is definitely an acquired
taste and can end up with you having text backwards after you turn the mode off

Figlet is only set up to work with ``fancytext_retro``. This is because the output is multi-line text
for individual words. It takes a ``font`` argument, you can use most `figlet fonts <http://www.figlet.org/examples.html>`_

Contributing
############

Want a new mode? Having problems?

Head to the `open source repository <https://github.com/psethwick/plover_fancytext>`_

Feel free to:

* Raise an issue
* Open a pull request, new modes accepted!
