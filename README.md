A simple cli hangman in python for fun

Example run: 

```
Would you like to provide a word or generate a random word? (1 = provide, 2 = random): 2

Word: _ _ _ _ _ _ _
Guessed: (none)
Lives remaining: 5
Guess a letter: a

a was in the word! There is/are 6 letter(s) remaining

Word: _ _ a _ _ _ _
Guessed: a
Lives remaining: 5
Guess a letter: s

s was in the word! There is/are 5 letter(s) remaining

Word: s _ a _ _ _ _
Guessed: a s
Lives remaining: 5
Guess a letter: t

t was in the word! There is/are 4 letter(s) remaining

Word: s t a _ _ _ _
Guessed: a s t
Lives remaining: 5
Guess a letter: r

r was in the word! There is/are 3 letter(s) remaining

Word: s t a _ _ _ r
Guessed: a r s t
Lives remaining: 5
Guess a letter: o

o was not in the word!

Word: s t a _ _ _ r
Guessed: a o r s t
Lives remaining: 4
Guess a letter: i

i was not in the word!

Word: s t a _ _ _ r
Guessed: a i o r s t
Lives remaining: 3
Guess a letter: c

c was not in the word!

Word: s t a _ _ _ r
Guessed: a c i o r s t
Lives remaining: 2
Guess a letter: a

You have already guessed this letter, please guess something else
Guess a letter: p

p was in the word! There is/are 2 letter(s) remaining

Word: s t a p _ _ r
Guessed: a c i o p r s t
Lives remaining: 2
Guess a letter: e

e was in the word! There is/are 1 letter(s) remaining

Word: s t a p _ e r
Guessed: a c e i o p r s t
Lives remaining: 2
Guess a letter: l

l was in the word! There is/are 0 letter(s) remaining

You won! The word was: stapler
```
