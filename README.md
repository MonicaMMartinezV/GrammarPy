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


## **Model of the Solution**

The next table represents the grammar implemented for this project following the python syntax of a “match case” statement.



MT
→
MS SPS VN SC IN CSS
CSS
→
|
CS CSS
CS DC
CS
→
|
|
|
CST SPS VN SC IN CD
CST SPS VN SPS SC IN CD
CST SPS NM SC IN CD
CST SPS NM SPS SC IN CD
DC
→
|
CST SPS US SC IN CD
CST SPS US SPS SC IN CD
CD
→
|
|
|
PNT PR CM EN CMM PL IN
VN SPS EQ SPS NM IN
VN SPS EQ SPS CM EN CMM IN
MT
EN
→
|
VN
VN SP EN
VN
→
|
|
|
LT VS
US VS
LT
US
VS
→
|
|
|
|
|
|
LT VS
LT
NM VS
NM
US VS
US
EP
TBS
→
TB+
TB
→
SP SP SP SP
IN
→
NL TBS
SPS
→
SP*
LT
→
|
"a" | "b" | ... | "z" | "A" 
"B" | ... | "Z"
NM
→
"0" | "1" | "2" | ... | "9"
MS
→
"match"
CST
→
"case"
PNT
→
"print"
SP
→
" "
SC
→
|
":"
":" " "*
NL
→
"~"
US
→
"_"
EQ
→
"="
EP
→
""
PR
→
"("
PL
→
")"
CM
→
"‘"
CMM
→
"’"




- an
- and
- anca
- anarya
- amil

In order to accept these words, I modeled the DFA, as follows:
![Automaton](automatonImage.jpg)

This automaton operates with the initial state "start" and two states, "s1" and "s2", which are designated as accepted states. Transitions are defined for each state and input symbol combination. This DFA is designed to accept words like "amil", "an", "anarya", "anca", and "and" from the Elvish language. 

*The presented automaton is equivalent to the following regular expression:*

DFA 1 -> RE 1: 

{^a(mil|n(d|arya|ca)?)$}

## **Implementation**
For my implementation of lexical analysis, I followed the structure defined in the "automatonElven15.pl" file. To use the file, you can input in two ways:

First, with the following format:

*dfa("amil").*

With this, the program should return *true* if it complies with the rules established in the automaton, and *false* if the string is not part of the language.

Some examples of inputs and outputs are: 
```
?- dfa('a').
[a]
false.

?- dfa("cdn").
[c,d,n]
false.

?- dfa("anarya").
[a,n,a,r,y,a]
true.

?- dfa("amil").
[a,m,i,l]
true.
```

Second, you can use the test cases from the "test.pl" file:

*Format:*

testStatusNumerodeltest.

*Example:*

testAccepted5.

In this case the program should return a message of what is expected, the string and the response provided by the automaton.

Some examples of inputs and outputs are: 
```
?- testRejected7.
Must be false: [a,n,n,a]
false.

?- testAccepted5.
Must be true: [a,m,i,l]
true.

?- testRejected4.
Must be false: [a,m,i,l,a]
false.

?- testAccepted3.
Must be true: [a,n,c,a]
true.
```

Here's a breakdown of how "automatonElven15.pl" file works:

- **States definition:** The automaton defines multiple states, including a starting state (start) and several intermediary states (s0 to s8).

- **Initial state:** The starting state is defined as 'start', indicating the initial point.

- **Accepted states:** States 's1' and 's2' are marked as accepted states, indicating that reaching these states signifies the successful recognition of an Elvish word.

- **Transitions:** Transitions between states are defined based on the input characters.

- **Acceptance function:** Defines the acceptance criteria for the input string. If the current state is an accepted state and the input string is empty, the word is accepted as an Elvish word.

- **Aux Function:** Initializes the acceptance process by starting from the initial state and recursively traversing the transitions based on the input characters.

- **DFA Function:** Converts a given string into a list of characters and initiates the acceptance process for each string. If the string is accepted, it returns true; otherwise, false.

## **Tests**
The "test.pl" file contains all the test cases for the automaton. You just need to follow these steps:
1. **Download and consult files:**

   You must download both files "automatonElven15.pl" and "test.pl". Then, open your SWI-Prolog application, where you will only consult the "test.pl" file.
   
2. **Call the function:**
  
   You should call the function of the test case you want to check, and a message will be displayed indicating the expected result, the word in question, and the response provided by the automaton, whether it is *true* or *false*.
   ```
   ?- testRejected7.
   Must be false: [a,n,n,a]
   false.
   ```
   
3. **Use this format:**

   testStatusNumerodeltest.
   
   *Example:*
   
   testAccepted5.

## **Analysis**
The complexity of this code primarily depends on the length of the input string and the number of transitions required to process it. Since Prolog operates on a non-deterministic and deterministic basis, and explores all possible paths, the complexity can be high for larger input strings or automata with many states and transitions. 

However, the complexity can be bounded by the size of the automaton and the length of the input string. The overall complexity of this is $O(n)$, where n is the length of the input string, because the program processes the input character by character, transitioning between states. This is equivalent to the next code:

```python
for element in list:  # Through the list
    print(element)
```

My first approach to the solution was to use an automaton in Prolog, which is also a natural solution. Initially, I constructed a DFA model with a total of 4 acceptance states, which, although maintaining complexity at $O(n)$, is suboptimal as it resulted in too many acceptance states. Upon redesigning and approaching the problem from a different perspective, I made a second approach to the problem, which only had 2 acceptance states. I choosed the second DFA design because it reduced the DFA code. Additionally, another approach I took to the problem was to create an equivalent regular expression and a automaton in python, which seemed like a valid option considering the $O(n)$ complexity of the automaton in prolog. However; based on the article of geeksforgeeks (GfG, 2023), unlike regular expressions, the DFA provides clear and specific rules for accepting or rejecting specific input strings, with each state and transition representing precise lexical patterns. In contrast, logical expressions may be harder to comprehend and maintain, especially for complex strings or languages with ambiguous rules. Additionally, the DFA offers efficient string verification through step-by-step analysis with deterministic transitions, ensuring fast and predictable processing, crucial for high-performance applications like large-scale text analysis.

## **References**
- FasterCapital (2021). NFA vs DFA desentranar las diferencias en los modelos de automata finitos. (https://fastercapital.com/es/contenido/NFA-vs--DFA--desentranar-las-diferencias-en-los-modelos-de-automata-finitos.html)
- OWTTA (2022). Elvish languages. One Wiki to Rule Them All. The Lord of the Rings Wiki.  (https://lotr.fandom.com/wiki/Elvish_languages)
- GfG (2023, January 28). Application of Deterministic Finite Automata (DFA). GeeksforGeeks. (https://www.geeksforgeeks.org/application-of-deterministic-finite-automata-dfa/)
