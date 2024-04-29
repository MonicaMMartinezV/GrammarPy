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


## **Models**

The next table represents the grammar implemented for this project following the python syntax of a “match case” statement.

| Non-terminal | Production |
|--------------|------------|
| MT           | MS SPS VN SC IN CSS |
| CSS          | CS CSS \| CS DC |
| CS           | CST SPS VN SC IN CD \| CST SPS VN SPS SC IN CD \| CST SPS NM SC IN CD \| CST SPS NM SPS SC IN CD |
| DC           | CST SPS US SC IN CD \| CST SPS US SPS SC IN CD |
| CD           | PNT PR CM EN CMM PL IN \| VN SPS EQ SPS NM IN \| VN SPS EQ SPS CM EN CMM IN \| MT |
| EN           | VN \| VN SP EN |
| VN           | LT VS \| US VS \| LT \| US |
| VS           | LT VS \| LT \| NM VS \| NM \| US VS \| US \| EP |
| TBS          | TB+ |
| TB           | SP SP SP SP |
| IN           | NL TBS |
| SPS          | SP* |
| LT           | "a" \| "b" \| ... \| "z" \| "A" \| "B" \| ... \| "Z" |
| NM           | "0" \| "1" \| "2" \| ... \| "9" |
| MS           | "match" |
| CST          | "case" |
| PNT          | "print" |
| SP           | " " |
| SC           | ":" \| ":" " "* |
| NL           | "~" |
| US           | "_" |
| EQ           | "=" |
| EP           | "" |
| PR           | "(" |
| PL           | ")" |
| CM           | "‘" |
| CMM          | "’" |

![parserError](GrammarModel.jpg)

Each non-terminal and its meaning are attached in the following table.

| Non-Terminal | Meaning           | Non-Terminal | Meaning           |
|--------------|-------------------|--------------|-------------------|
| MT           | Match             | NM           | Number            |
| CSS          | Cases             | MS           | Match String      |
| CS           | Case              | CST          | Case String       |
| DC           | Default Case      | PNT          | Print             |
| CD           | Code              | SP           | Space             |
| EN           | Enunciate         | SC           | Space Colon       |
| VN           | Variable Name     | NL           | New Line          |
| VS           | Variable String   | US           | Underscore        |
| TBS          | Tabs              | EQ           | Equality          |
| TB           | Tab               | EP           | Epsilon           |
| IN           | Indentation       | PR           | Right Parenthesis |
| SPS          | Spaces            | PL           | Left Parenthesis  |
| SPSP         | Spaces Prime      | CM           | Comma Left        |
| LT           | Letter            | CMM          | Comma Right       |

The grammar operates under certain assumptions. Firstly, it assumes that the "match case" statement does not include any preceding code unrelated to these statements and begins directly with "match". Additionally, other lines of code valid for Python but not pertaining to "match case" statements will not be accepted. Inside the “match case” block the rules implemented with the grammar are the following.

- Match and case statements are next to a user-defined variable following a colon. Other valid Python alternatives to this, such as using an object instead of a variable, were not considered.
  *match var1:  -> Accepted*
  *match Person(age=19,Name="Pedro"):`  -> Not accepted*
- Case statement must be on a new line followed by at least a single “tab” (which was defined as four blank spaces concatenated).
- Case can be followed by a number, but only one digit.
  *case 1:  -> Accepted*
  *case 15:`  -> Not accepted*
- All “match” statements must have at least a default case.
- All “case” statements must be followed by a new line and at least a single “tab”.
- Case only have three valid Python code lines:
  - Print with only text inside.
    *print('Test') -> Accepted*
    *print(var1) -> Not accepted*
  - Variable assignments with only a variable and a string or a variable and a number.
    *var1 = 'Test'  -> Accepted*
    *var1 = var2  -> Not accepted*
  - Another “match case” set.
- Default case statements are followed by an underscore “_” and a colon.
- The default case has the same rules as the other types of cases.
- End of the code must be a statement, it must not be left blank.
  *case _:*
        *print('Test')  -> Accepted*
  *case _:  -> Not accepted*

The previously described ruleset was implemented into the CFG that works with separated characters, which means that the strings are analyzed one character at a time. It's necessary because a tokenizer designed for whole strings cannot effectively handle user-defined variables or strings, as each string must undergo a character-by-character analysis. Previous designs involved defining a set of variable names that a user can use instead of leaving it open, with the assumptions of following Python rules for variables.

| Non-terminal | Production |
|--------------|------------|
| S            | MT |
| MT           | MTS SP SPS VAR SPS CL NL TBS |
| VAR          | "var1" \| "var2" |
| LT           | "a" \| "b" \| ... \| "z" \| "A" \| "B" \| ... \| "Z" |
| MTS          | "match" |
| SPS          | SP SPS \| SP \| ᵋ |
| SP           | " " |
| TBS          | TB TBS \| TB |
| TB           | SP SP SP SP |
| NL           | "~" |
| IN           | NL TB |
| CL           | ":" |

When applying the previous grammar with the sentence tokenizer "punkt", the test codes are tokenized into words and certain special characters. However, this process may result in the loss of all new lines and blank spaces. To meet the previously established requirements, the implementation must be capable of verifying the presence of new lines and tabs according to the specified rule set. Because of this, it was decided to implement the CFG with a letter by letter based parser, which allows checking user-defined strings and variables, spaces and newlines are not deleted and special characters are preserved to be analyzed by the parser.

Regarding ambiguity, while implementing the CFG, certain ambiguous lines were encountered, particularly when handling cases with identical conditions. The following test code exemplifies this issue.

```python
match var_name1:
    case 4  :
    case 5:
    case 5:
    case 5:
    case 5:
    case 5:
```

This led the parser to produce a duplicated three as the next image shows.
![parserError](TestError.jpg)

To address this issue, a default case requirement was introduced to ensure the acceptance of the code, allowing the CFG to either converge or reject the test code. Ambiguity can also arise from left recursion, which was mitigated by crafting the grammar with a focus on right recursion exclusively. Left recursion was encountered only once, involving the concatenation of multiple spaces between "case" and the subsequent number or variable. These types of adjustments to resolve left recursion were rare.


## **Implementation**

The CFG was implemented by using the nltk python module, some changes were done to make it work with the library, the main ones being the definitions of the letters and numbers. The module has to have the whole alphabet and numbers digit by digit defined, the same goes for reserved words like “match”, “case” and “print”.

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

**LL1 parsing and a specific string**
To ensure the correctness of the grammar and parser implementation, I analyzed a representative test. This test is accompanied by the results of LL(1) parsing, demonstrating the correctness of the parsing algorithm.

For performing an LL(1) analysis of the given grammar, we first need to calculate the FIRST and FOLLOW sets for each non-terminal symbol. Then, with that information, we can construct the parsing table. When calculating the FOLLOW sets, the following rules were followed:

![parserError](rulesFollow.jpg)

Having computed the FIRST and FOLLOW sets for each non-terminal symbol according to the aforementioned rules, it resulted in a table that, due to its dimensions, cannot be directly screenshot. This table is located on the first page of the Google Sheets document named "FFT (First and follow table)" at the following link:
https://docs.google.com/spreadsheets/d/1WKnLy_EaHy_fjLwgSlaqiky6YbcslpDvQz8Ll8si1Ww/edit?usp=sharing

With this table in hand, I conducted two LL(1) parsing tasks:
- General LL(1) Parsing: The first set of tests involves performing LL(1) parsing on the grammar itself. This demonstrates the correctness of the parsing table generated from the grammar rules. This table is located on the second page of the Google Sheets document named "LL1 general (Left Left Lookahead 1 general)" at the following link:
  https://docs.google.com/spreadsheets/d/1WKnLy_EaHy_fjLwgSlaqiky6YbcslpDvQz8Ll8si1Ww/edit?usp=sharing

- Specific String LL(1) Parsing: The second set of tests involves performing LL(1) parsing on a specific string defined within the grammar domain. This test showcases the ability of the parser to correctly identify the syntactic structure of the input string. This table is located on the third page of the Google Sheets document named "LL1 example (Left Left Lookahead 1 example)" at the following link:
https://docs.google.com/spreadsheets/d/1WKnLy_EaHy_fjLwgSlaqiky6YbcslpDvQz8Ll8si1Ww/edit?usp=sharing

To provide more tests that should be and shouldn't be accepted by this grammar, I created the test.txt file. It contains additional tests that, when copied into the NLTK code, will deploy the respective LL(1) parser. The tests marked as "rejected" in the .txt file indicate that when you copy the test into the code, it shouldn't deploy anything. This means the grammar didn't accept the test. All you need to do to run the tests is copy them one by one into this code section:

```python
parser = nltk.ChartParser(grammar)

# Here you copy the test, be careful with all the tabs, spaces and symbols
text = """match _var_name1:
    case 1:
        match varName2:
            case 1:
                match varName2:
                    case 1:
                        var = 'Hola Mundo'
                    case _:
                        print('Adios')
            case _:
                print('Adios')
    case 2:
        var = 'Hola Mundo'
    case 3:
        var = 0
    case _:
        print('Hola Benji')
        """
```

## **References**
