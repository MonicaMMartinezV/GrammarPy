# GrammarPy

# **AutomatonElvish15: E1 Implementation of Lexical Analysis (Automaton and Regular Expression)**
Automaton and regular expression that recognizes the elvish language.

## Description

I choose the Elven language form the Lord of the Rings Saga. This language is fictional, originating from fantasy literature such as J.R.R. Tolkien's Middle-earth universe, referred to as a language spoken by elves in that universe (OWTTA, 2022). The modeling technique I decided to use was a DFA because, based in the FasterCapital article (FasterCapital, 2021), DFAs accurately capture the deterministic rules of word formation and syntax, making them ideal for representing the language's grammar and vocabulary. Additionally, DFAs allow for formal analysis and validation of the language's rules, ensuring scalability and ease of maintenance as the language evolves over time.

## Model of the Solution

The provided automaton is designed to recognize words in the Elvish language. It consists of several states representing different stages of recognizing a valid Elvish word. The accepted cases are:

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

## Implementation
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

## Tests
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

## Analysis
The complexity of this code primarily depends on the length of the input string and the number of transitions required to process it. Since Prolog operates on a non-deterministic and deterministic basis, and explores all possible paths, the complexity can be high for larger input strings or automata with many states and transitions. 

However, the complexity can be bounded by the size of the automaton and the length of the input string. The overall complexity of this is $O(n)$, where n is the length of the input string, because the program processes the input character by character, transitioning between states. This is equivalent to the next code:

```python
for element in list:  # Through the list
    print(element)
```

My first approach to the solution was to use an automaton in Prolog, which is also a natural solution. Initially, I constructed a DFA model with a total of 4 acceptance states, which, although maintaining complexity at $O(n)$, is suboptimal as it resulted in too many acceptance states. Upon redesigning and approaching the problem from a different perspective, I made a second approach to the problem, which only had 2 acceptance states. I choosed the second DFA design because it reduced the DFA code. Additionally, another approach I took to the problem was to create an equivalent regular expression and a automaton in python, which seemed like a valid option considering the $O(n)$ complexity of the automaton in prolog. However; based on the article of geeksforgeeks (GfG, 2023), unlike regular expressions, the DFA provides clear and specific rules for accepting or rejecting specific input strings, with each state and transition representing precise lexical patterns. In contrast, logical expressions may be harder to comprehend and maintain, especially for complex strings or languages with ambiguous rules. Additionally, the DFA offers efficient string verification through step-by-step analysis with deterministic transitions, ensuring fast and predictable processing, crucial for high-performance applications like large-scale text analysis.

## References
- FasterCapital (2021). NFA vs DFA desentranar las diferencias en los modelos de automata finitos. (https://fastercapital.com/es/contenido/NFA-vs--DFA--desentranar-las-diferencias-en-los-modelos-de-automata-finitos.html)
- OWTTA (2022). Elvish languages. One Wiki to Rule Them All. The Lord of the Rings Wiki.  (https://lotr.fandom.com/wiki/Elvish_languages)
- GfG (2023, January 28). Application of Deterministic Finite Automata (DFA). GeeksforGeeks. (https://www.geeksforgeeks.org/application-of-deterministic-finite-automata-dfa/)
