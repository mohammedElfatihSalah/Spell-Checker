# Spell-Checker
Spell checker for project created by by Dan Jurafsky

We will be using the writings of secondary-school children, collected by David Holbrook. The training data is located in the data/ directory. A summary of the contents:

- holbrook-tagged-train.dat: the corpus to train your language models

- holbrook-tagged-dev.dat: a corpus of spelling errors for development

- count_1edit.txt : a table listing counts of edits x|w, taken from Wikipedia. You don't need to modify any code which uses this. 

## Modules

- SpellCorrect.py: Computes the most likely correction given a language model and edit model. The main() function here will load all of your language model and print performance on the development data, useful for debugging. It may be useful to comment out some of the tests in main() when developing.

- EditModel.py: Reads the count_1edit.txt file and computes the probability of corrections. The candidate corrections are all strings within Damerau-Levenshtein edit distance 1. The probability of no correction is set at .9 (P(x|x)=.9). Note that the EditModel isn't great, but your language models will be evaluated using this model, so it won't effect your grade.

- HolbrookCorpus.py: Reads in the corpus and generates test cases from misspellings.

- Sentence.py: Holds the data for a given sentence, which is a list of Datums. Contains helper functions for generating the correct sentence and the sentence with the spelling error.

- Datum.py: Contains two strings, word and error. The word is the corrected word, and error contains the spelling error. For tokens which are spelled correctly in the corpus, error = ''. 
- LanguageModel.py: given a sentence it calculates its joint probability ( Implemented here LaplaceUnigram, LaplaceBigram, and StupidBackoff)

Here is the architecture of the system


<img src = 'https://github.com/mohammedElfatihSalah/Spell-Checker/blob/main/uml.png?raw=true' width=1200 height=800/>
