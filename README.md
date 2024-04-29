# **GrammarPy: E2 Generating and Cleaning a Restricted Context Free Grammar**

A grammar that that recognizes the Python language.


## **Description**

Programming languages consist of various components, including syntax, semantics, and a predefined set of rules and reserved keywords for correct execution. Consequently, crafting a grammar for any language can be both interesting and challenging. In this project, a grammar was created to verify  'match case' statements following Python's rule set.

Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. The last two characteristics listed are due to a clear and concise syntax, which emphasizes readability and reduces the cost of program maintenance. Python code is typically easy to understand, even for those new to programming, due to its use of meaningful indentation and English-like keywords.

Indentation is a huge component of the language, instead of using brackets or , in the newer versions of the language, this consists of four blank spaces before any nested operations instead of using curly brackets, this makes the code more readable and can be more easy to follow.

A normal Python “match case” statement can be seen in the following code snippet:
```python
match parameter:
    case first:
        var1 = var2
    case second:
        do_something1(second)
    case third:
        match parameter2:
            case nested_f:
                do_something2_1(first)
            case _:
                nothing_matched_function()
    case n:
        do_something4(n)
    case _:
        nothing_matched_function()
```
The syntax of the language can be seen in the previous example, where the reserved words “match” and “case” are next to a user-defined variable following the next rules:
1. Any variable has to start with a letter or underscore.
2. The only special character allowed here is underscore (“_”).
3. It cannot start with a number but can contain it anywhere on the variable name.
4. Variables are case sensitive.

Both “match” and “case” can also take strings and numbers as the parameters. Continuing the syntax rules, “case” should be preceded by the indentation with respect to the indentation of the “match”; it always has to be a tab more of the “match” indentation. A “case” followed by underscore is determined to be a default case and it must be there for every “match” in the code. The statements inside each “case” can be any python pattern that follows the structure of assignment, function calls, etc. However the prohibited patterns are function and class definitions, and library importations.

# Examples of valid “match case” statements.

```python
match var_1:
    case 1:
        print("Path 1")
    case 2:
        print("Path 2")
    case _:
        print("Default")
```
In this case if the var_1 has a numeric value of two, the output of the script will be “Path 2”.

```python
match var_1:
    case "Path 1":
        print("1")
    case "Path 2":
        print("2")
    case _:
        print("Default")
```
In this case if the var_1 has a string with value “Path 1”, the output of the script will be “1”.

```python
match var_1:
    case 1:
        print("Path 1")
    case 2:
        print("Path 2")
    case _:
        match var_2:
            case 1:
                print("Path 3.1")
            case 2:
                print("Path 3.2")
            case _:
                print("Path 3.Default")
```
In this example if the var_1 has an integer value of 3, and var_2 has the same value as val_1, the output of the script will be “Path 3.Default”.


<a name="_nbdgdid9urzo"></a>Models

The next table represents the grammar implemented for this project following the python syntax of a “match case” statement.

|MT|→|MS SPS VN SC IN CSS|
| :- | :- | :- |
|CSS|<p>→</p><p>|</p>|<p>CS CSS</p><p>CS DC</p>|
|CS|<p>→</p><p>|</p><p>|</p><p>|</p>|<p>CST SPS VN SC IN CD</p><p>CST SPS VN SPS SC IN CD</p><p>CST SPS NM SC IN CD</p><p>CST SPS NM SPS SC IN CD</p>|
|DC|<p>→</p><p>|</p>|<p>CST SPS US SC IN CD</p><p>CST SPS US SPS SC IN CD</p>|
|CD|<p>→</p><p>|</p><p>|</p><p>|</p>|<p>PNT PR CM EN CMM PL IN</p><p>VN SPS EQ SPS NM IN</p><p>VN SPS EQ SPS CM EN CMM IN</p><p>MT</p>|
|EN|<p>→</p><p>|</p>|<p>VN</p><p>VN SP EN</p>|
|VN|<p>→</p><p>|</p><p>|</p><p>|</p>|<p>LT VS</p><p>US VS</p><p>LT</p><p>US</p>|
|VS|<p>→</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p>|<p>LT VS</p><p>LT</p><p>NM VS</p><p>NM</p><p>US VS</p><p>US</p><p>EP</p>|
|TBS|→|TB+|
|TB|→|SP SP SP SP|
|IN|→|NL TBS|
|SPS|→|SP\*|
|LT|<p>→</p><p>|</p>|<p>"a" | "b" | ... | "z" | "A" </p><p>"B" | ... | "Z"</p>|
|NM|→|"0" | "1" | "2" | ... | "9"|
|MS|→|"match"|
|CST|→|"case"|
|PNT|→|"print"|
|SP|→|" "|
|SC|<p>→</p><p>|</p>|<p>":"</p><p>":" " "\*</p>|
|NL|→|"~"|
|US|→|"\_"|
|EQ|→|"="|
|EP|→|""|
|PR|→|"("|
|PL|→|")"|
|CM|→|"‘"|
|CMM|→|"’"|

Each non-terminal and its meaning are attached in the following table.

The grammar operates under certain assumptions. Firstly, it assumes that the "match case" statement does not include any preceding code unrelated to these statements and begins directly with "match". Additionally, other lines of code valid for Python but not pertaining to "match case" statements will not be accepted. Inside the “match case” block the rules implemented with the grammar are the following.

- Match and case statements are next to a user-defined variable following a colon. Other valid Python alternatives to this, such as using an object instead of a variable, were not considered.
  - `match var1:`  -> Accepted
  - `match Person(age=19,Name="Pedro"):`  -> Not accepted

- Case statement must be on a new line followed by at least a single “tab” (which was defined as four blank spaces concatenated).
  - Case can be followed by a number, but only one digit.
    - `case 1:`  -> Accepted
    - `case 15:`  -> Not accepted

- All “match” statements must have at least a default case.

- All “case” statements must be followed by a new line and at least a single “tab”.

- Case only have three valid Python code lines:
  - Print with only text inside.
    - `print('Test')`  -> Accepted
    - `print(var1)`  -> Not accepted
  - Variable assignments with only a variable and a string or a variable and a number.
    - `var1 = 'Test'`  -> Accepted
    - `var1 = var2`  -> Not accepted

- Another “match case” set.

- Default case statements are followed by an underscore “_” and a colon.
  - The default case has the same rules as the other types of cases.

- End of the code must be a statement, it must not be left blank.
  - ``
    case _:
        print('Test')    -> Accepted
    case _:  -> Not accepted
    ``
The previously described ruleset was implemented into the CFG that works with separated characters, which means that the strings are analyzed one character at a time. It's necessary because a tokenizer designed for whole strings cannot effectively handle user-defined variables or strings, as each string must undergo a character-by-character analysis. Previous designs involved defining a set of variable names that a user can use instead of leaving it open, with the assumptions of following Python rules for variables.

In order to accept these words, I modeled the DFA, as follows:
![Automaton](automatonImage.jpg)



## **Implementation**

The CFG was implemented by using the nltk python module, some changes were done to make it work with the library, the main ones being the definitions of the letters and numbers. The module has to have the whole alphabet and numbers digit by digit defined, the same goes for reserved words like “match”, “case” and “print”. Left recursion was

```python
"""
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
    SPS -> SP SPSP | SP
    SPSP -> SP SPSP | EP
    LT -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
    NM -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    MS -> "m" "a" "t" "c" "h"
    CST -> "c" "a" "s" "e"
    PNT -> "p" "r" "i" "n" "t"
    SP -> " "
    SC -> ":" | SPS ":"
    NL -> "~"
    US -> "_"
    EQ -> "="
    EP -> ""
    PR -> "("
    PL -> ")"
    CM -> "'"
    CMM -> "'"
"""
```

## **Tests**

The following set of tests are designed to test the proposed ruleset and some of the properties of the “match case” statements. Each of the tests represents a valid Python "match case" code block, indicating that the CFG will accept them if all the rules are properly implemented within the constraints detailed on this project.

**Test 1.**

## **Analysis**


## **References**
