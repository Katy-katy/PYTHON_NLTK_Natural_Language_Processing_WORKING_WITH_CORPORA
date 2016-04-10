# PYTHON_NLTK_Natural_Language_Processing_WORKING_WITH_CORPORA
Tokenization, applying Part-of-Speech tagger, finding the frequency of each word and frequency of each word given it’s part-of-speech tag; finding the words used in the similar context and the most common collocations

This program was written as the first programming assignment for "Natural Language Processing" class at University of California Santa Cruz.

The program reads analyze two different narrative corpora. The first corpora is a collection of 26 Aesop’s 
fables. The second corpus is a collection of 12 personal narratives from some weblogs. Both corpora are provided as 
zip archives with each individual file containing a different fable or blog.

The program takes one command line argument that specifies which corpus will be analyzed. 
1. Tokenization
The program delimits the sentences for each document in the corpus.Then it tokenize the words in each sentence of each 
document and count the number of total words in the corpus and write the result to stdout.
2. Part-of-Speech
The program apply the default part-of-speech tagger to each tokenized sentence.Then it writes a file named
CORPUS NAME-pos.txt that has each part-of-speech tagged sentence on a separate line and a blank newline separating documents. Where CORPUS NAME is either fables or blogs. The format of the tagging should be a word-tag pair with a / in between. For example: The/DT boy/NN jumped/VBD ./.
3. Frequency
The program writes the vocabulary size of corpus to stdout, writes the most frequent part-of-speech tag and its frequency
to the stdout, finds the frequency of each unique word. Then it writes the list in decreasing order to a file named 
CORPUS NAME-word-freq.txt. Then it finds  the frequency of each word given it’s part-of-speech tag using a conditional 
frequency distribution and writes the results to a file named CORPUS NAME-pos-word-freq.txt.
4. Similar Words
For the most frequent word in the NN (nouns), VBD (past-tense verbs), JJ (adjectives) and RB (adjectives) part-of-speech
tags the program finds the most similar words using Text.similar() and writes the output to stdout.
5. Collocations
The program writes the collocations to the stdout.
