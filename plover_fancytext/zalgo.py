import random

MARKS = [
    '\u0300',  # ̀ 	768 	Combining Grave Accent
    '\u0301',  # ́ 	769 	Combining Acute Accent
    '\u0302',  # ̂ 	770 	Combining Circumflex Accent
    '\u0303',  # ̃ 	771 	Combining Tilde
    '\u0304',  # ̄ 	772 	Combining Macron
    '\u0305',  # ̅ 	773 	Combining Overline
    '\u0306',  # ̆ 	774 	Combining Breve
    '\u0307',  # ̇ 	775 	Combining Dot Above
    '\u0308',  # ̈ 	776 	Combining Diaeresis
    '\u0309',  # ̉ 	777 	Combining Hook Above
    '\u030A',  # ̊ 	778 	Combining Ring Above
    '\u030B',  # ̋ 	779 	Combining Double Acute Accent
    '\u030C',  # ̌ 	780 	Combining Caron
    '\u030D',  # ̍ 	781 	Combining Vertical Line Above
    '\u030E',  # ̎ 	782 	Combining Double Vertical Line Above
    '\u030F',  # ̏ 	783 	Combining Double Grave Accent
    '\u0310',  # ̐ 	784 	Combining Candrabindu
    '\u0311',  # ̑ 	785 	Combining Inverted Breve
    '\u0312',  # ̒ 	786 	Combining Turned Comma Above
    '\u0313',  # ̓ 	787 	Combining Comma Above
    '\u0314',  # ̔ 	788 	Combining Reversed Comma Above
    '\u0315',  # ̕ 	789 	Combining Comma Above Right
    '\u0316',  # ̖ 	790 	Combining Grave Accent Below
    '\u0317',  # ̗ 	791 	Combining Acute Accent Below
    '\u0318',  # ̘ 	792 	Combining Left Tack Below
    '\u0319',  # ̙ 	793 	Combining Right Tack Below
    '\u031A',  # ̚ 	794 	Combining Left Angle Above
    '\u031B',  # ̛ 	795 	Combining Horn
    '\u031C',  # ̜ 	796 	Combining Left Half Ring Below
    '\u031D',  # ̝ 	797 	Combining Up Tack Below
    '\u031E',  # ̞ 	798 	Combining Down Tack Below
    '\u031F',  # ̟ 	799 	Combining Plus Sign Below
    '\u0320',  # ̠ 	800 	Combining Minus Sign Below
    '\u0321',  # ̡ 	801 	Combining Palatalized Hook Below
    '\u0322',  # ̢ 	802 	Combining Retroflex Hook Below
    '\u0323',  # ̣ 	803 	Combining Dot Below
    '\u0324',  # ̤ 	804 	Combining Diaeresis Below
    '\u0325',  # ̥ 	805 	Combining Ring Below
    '\u0326',  # ̦ 	806 	Combining Comma Below
    '\u0327',  # ̧ 	807 	Combining Cedilla
    '\u0328',  # ̨ 	808 	Combining Ogonek
    '\u0329',  # ̩ 	809 	Combining Vertical Line Below
    '\u032A',  # ̪ 	810 	Combining Bridge Below
    '\u032B',  # ̫ 	811 	Combining Inverted Double Arch Below
    '\u032C',  # ̬ 	812 	Combining Caron Below
    '\u032D',  # ̭ 	813 	Combining Circumflex Accent Below
    '\u032E',  # ̮ 	814 	Combining Breve Below
    '\u032F',  # ̯ 	815 	Combining Inverted Breve Below
    '\u0330',  # ̰ 	816 	Combining Tilde Below
    '\u0331',  # ̱ 	817 	Combining Macron Below
    '\u0332',  # ̲ 	818 	Combining Low Line
    '\u0333',  # ̳ 	819 	Combining Double Low Line
    '\u0334',  # ̴ 	820 	Combining Tilde Overlay
    '\u0335',  # ̵ 	821 	Combining Short Stroke Overlay
    '\u0336',  # ̶ 	822 	Combining Long Stroke Overlay
    '\u0337',  # ̷ 	823 	Combining Short Solidus Overlay
    '\u0338',  # ̸ 	824 	Combining Long Solidus Overlay
    '\u0339',  # ̹ 	825 	Combining Right Half Ring Below
    '\u033A',  # ̺ 	826 	Combining Inverted Bridge Below
    '\u033B',  # ̻ 	827 	Combining Square Below
    '\u033C',  # ̼ 	828 	Combining Seagull Below
    '\u033D',  # ̽ 	829 	Combining X Above
    '\u033E',  # ̾ 	830 	Combining Vertical Tilde
    '\u033F',  # ̿ 	831 	Combining Double Overline
    '\u0340',  # ̀ 	832 	Combining Grave Tone Mark
    '\u0341',  # ́ 	833 	Combining Acute Tone Mark
    '\u0342',  # ͂ 	834 	Combining Greek Perispomeni
    '\u0343',  # ̓ 	835 	Combining Greek Koronis
    '\u0344',  # ̈́ 	836 	Combining Greek Dialytika Tonos
    '\u0345',  # ͅ 	837 	Combining Greek Ypogegrammeni
    '\u0346',  # ͆ 	838 	Combining Bridge Above
    '\u0347',  # ͇ 	839 	Combining Equals Sign Below
    '\u0348',  # ͈ 	840 	Combining Double Vertical Line Below
    '\u0349',  # ͉ 	841 	Combining Left Angle Below
    '\u034A',  # ͊ 	842 	Combining Not Tilde Above
    '\u034B',  # ͋ 	843 	Combining Homothetic Above
    '\u034C',  # ͌ 	844 	Combining Almost Equal To Above
    '\u034D',  # ͍ 	845 	Combining Left Right Arrow Below
    '\u034E',  # ͎ 	846 	Combining Upwards Arrow Below
    '\u034F',  # ͏ 	847 	Combining Grapheme Joiner
    '\u0350',  # ͐ 	848 	Combining Right Arrowhead Above
    '\u0351',  # ͑ 	849 	Combining Left Half Ring Above
    '\u0352',  # ͒ 	850 	Combining Fermata
    '\u0353',  # ͓ 	851 	Combining X Below
    '\u0354',  # ͔ 	852 	Combining Left Arrowhead Below
    '\u0355',  # ͕ 	853 	Combining Right Arrowhead Below
    '\u0356',  # ͖ 	854 	Combining Right Arrowhead And Up Arrowhead Below
    '\u0357',  # ͗ 	855 	Combining Right Half Ring Above
    '\u0358',  # ͘ 	856 	Combining Dot Above Right
    '\u0359',  # ͙ 	857 	Combining Asterisk Below
    '\u035A',  # ͚ 	858 	Combining Double Ring Below
    '\u035B',  # ͛ 	859 	Combining Zigzag Above
    '\u035C',  # ͜ 	860 	Combining Double Breve Below
    '\u035D',  # ͝ 	861 	Combining Double Breve
    '\u035E',  # ͞ 	862 	Combining Double Macron
    '\u035F',  # ͟ 	863 	Combining Double Macron Below
    '\u0360',  # ͠ 	864 	Combining Double Tilde
    '\u0361',  # ͡ 	865 	Combining Double Inverted Breve
    '\u0362',  # ͢ 	866 	Combining Double Rightwards Arrow Below
    '\u0363',  # ͣ 	867 	Combining Latin Small Letter A
    '\u0364',  # ͤ 	868 	Combining Latin Small Letter E
    '\u0365',  # ͥ 	869 	Combining Latin Small Letter I
    '\u0366',  # ͦ 	870 	Combining Latin Small Letter O
    '\u0367',  # ͧ 	871 	Combining Latin Small Letter U
    '\u0368',  # ͨ 	872 	Combining Latin Small Letter C
    '\u0369',  # ͩ 	873 	Combining Latin Small Letter D
    '\u036A',  # ͪ 	874 	Combining Latin Small Letter H
    '\u036B',  # ͫ 	875 	Combining Latin Small Letter M
    '\u036C',  # ͬ 	876 	Combining Latin Small Letter R
    '\u036D',  # ͭ 	877 	Combining Latin Small Letter T
    '\u036E',  # ͮ 	878 	Combining Latin Small Letter V
    '\u036F',  # ͯ 	879 	Combining Latin Small Letter X
]


class Zalgo():

    def add_combining_marks(self, c: str) -> str:
        for m in random.sample(MARKS, random.randrange(1, 3)):
            c += m
        return c

    def __call__(self, str) -> str:
        if str:
            return ''.join(self.add_combining_marks(s) for s in str)
        return None


zalgo = Zalgo()
