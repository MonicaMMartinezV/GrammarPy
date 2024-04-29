import nltk

grammar = nltk.CFG.fromstring("""
    MT -> MS SPS VN SC IN CSS
    CSS -> CS CSS | CS DC
    CS -> CST SPS VN SC IN CD | CST SPS VN SPS SC IN CD | CST SPS NM SC IN CD | CST SPS NM SPS SC IN CD
    DC -> CST SPS US SC IN CD | CST SPS US SPS SC IN CD
    CD -> PNT PR CM EN CMM PL IN | VN SPS EQ SPS NM IN | VN SPS EQ SPS CM EN CMM IN
    EN -> VN | VN SP EN
    VN -> LT VS | LT
    VS -> LT VS | LT | NM VS | NM | US VS | US | EP
    TBS -> TB TBS | TB
    TB -> SP SP SP SP
    IN -> NL TBS
    LT -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
    NM -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    MS -> "m" "a" "t" "c" "h"
    CST -> "c" "a" "s" "e"
    PNT -> "p" "r" "i" "n" "t"
    SPS -> SP SPS | SP
    SP -> " "
    SC -> ":" | SP ":"
    NL -> "~"
    US -> "_"
    EQ -> "="
    EP -> ""
    PR -> "("
    PL -> ")"
    CM -> "'"
    CMM -> "'"
""")

# Test the CFG
parser = nltk.ChartParser(grammar)

text = """match var_name1:
    case 4:
        var = 4
    case 5:
        var = 'nose que poner'
    case _:
        print('Juana la cubana')
        """

text = text.replace('\n','~')

for tree in parser.parse([*text]):
    tree.pretty_print()