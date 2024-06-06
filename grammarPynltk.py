import nltk

def parse_grammar(text):
    """
    Parse a given text using the predefined context-free grammar (CFG) and
    check its validity.

    This function uses NLTK's ChartParser to parse the text according to a
    specified CFG. If the text conforms to the grammar, it prints a message
    and the parse trees; otherwise, it indicates that the text is not valid.

    Args:
        text (str): The text to be parsed.

    Returns:
        None
    """

    # Define the grammar using NLTK's CFG fromstring method
    grammar = nltk.CFG.fromstring("""
        MT -> MS SPS VN SC IN CSS
        CSS -> CS CSS | CS DC
        CS -> CST SPS VN SC IN CD | CST SPS VN SPS SC IN CD | CST SPS NM SC IN CD | CST SPS NM SPS SC IN CD
        DC -> CST SPS US SC IN CD | CST SPS US SPS SC IN CD
        CD -> PNT PR CM EN CMM PL IN | VN SPS EQ SPS NM IN | VN SPS EQ SPS CM EN CMM IN | MT
        EN -> VN | VN SP EN
        VN -> LT VS | US VS | LT | US
        VS -> LT VS | LT | NM VS | NM | US VS | US | EP
        TBS -> TB TBS | TB
        TB -> SP SP SP SP
        IN -> NL TBS
        SPS -> SP SPS | SP
        LT -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
        NM -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
        MS -> "m" "a" "t" "c" "h"
        CST -> "c" "a" "s" "e"
        PNT -> "p" "r" "i" "n" "t"
        SP -> " "
        SC -> ":" | SPS ":"
        NL -> "~"
        US -> "_"
        EQ -> "=" | SPS "=" SPS
        EP -> ""
        PR -> "("
        PL -> ")"
        CM -> "'"
        CMM -> "'"
    """)

    # Initialize the parser with the given grammar
    parser = nltk.ChartParser(grammar)
    # Replace newline characters with the '~' symbol as per the grammar
    # definition
    text = text.replace('\n', '~')

    try:
        # Attempt to parse the tokenized text
        trees = list(parser.parse([*text]))

        # Check if any parse trees were generated
        if trees:
            print("The text provided is valid. LL(1) parsing:")
            # Print each parse tree
            for tree in trees:
                tree.pretty_print()
        else:
            print("The text provided is not valid. Unable to parse.")
    except ValueError:
        print("The text provided is not valid. Unable to parse.")
