#Author: Ekaterina Tcareva
#CMRS_143, UCSC
#April 8, 2016

#!/usr/bin/env python

import nltk, zipfile, argparse
#python3 assignment1-stub-s16.py  --corpus fables
###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive.
# It first creates a ZipFile object.
# Using a list comprehension it creates a list where each element contains
# the raw text of the fable file.
# We iterate over each named file in the archive:
#     for fn in zip_archive.namelist()
# For each file that ends with '.txt' we open the file in read only
# mode:
#     zip_archive.open(fn, 'rU')
# Finally, we read the raw contents of the file:
#     zip_archive.open(fn, 'rU').read()
def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    contents = [zip_archive.open(fn, 'rU').read().decode('utf-8') for fn in zip_archive.namelist() if fn.endswith(".txt")]
    return contents

###############################################################################
## Stub Functions #############################################################
###############################################################################
def process_corpus(corpus_name):
    input_file = corpus_name + ".zip"
    corpus_contents = unzip_corpus(input_file)
    return corpus_contents

###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 1')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',  help='Which corpus to process {fables, blogs}')

    args = parser.parse_args()
      
    corpus_name = args.corpus
    
    if corpus_name == "fables" or "blogs":
        data = process_corpus(corpus_name)
    else:
        print("Unknown corpus name: {0}".format(corpus_name))
    
    #some parts of code above this point was provided for us, the code below is my own work
      
    #Write the name of the corpus to stdout
    print ("The courpus name is ", end = "")
    print (corpus_name)
   
    #Delimit the sentences for each document in the corpus.
      
    # let's keep texts as sentences in a new object
    data_sent = []
    for d in data:
    	d = nltk.sent_tokenize(d)
    	data_sent.append(d)
    
    #Tokenize the words in each sentence of each document
    data_tokens =[]# to keep tokens by sentences
    for text in data_sent:
    	tokens = []
    	for sent in text:    		
    		s = nltk.word_tokenize(sent)
    		tokens.append(s)
    	data_tokens.append(tokens)
    
    #Count the number of total words in the corpus and write the result to stdout.
    count = 0
    for t in data_tokens:
    	for a in t:
    		s = len(a)
    		count = count + s	
    print ("The number of words in the corpus is ", end = "")
    print(count)

    #Apply the default part-of-speech tagger to each tokenized sentence
    #let's keet it in data_speech array:
    data_speech = []
    for t in data_tokens:
    	parts = []
    	for a in t:
    		tag = nltk.pos_tag(a)
    		parts.append(tag)
    		#print(tag)
    	data_speech.append(parts)
    
    #Write a file named CORPUS NAME-pos.txt that has each part-of-speech tagged sentence 
    #on a separate line and a blank newline separating documents. Where CORPUS NAME is 
    #either fables or blogs. The format of the tagging should be a word-tag pair with a / 
    #in between. For example: The/DT boy/NN jumped/VBD ./.
    file_name = corpus_name + "-pos.txt"
    out_file = open(file_name, 'w')
    for t in data_speech:
    	for s in t:
    		for w in s:
    			my_st = w[0] + "/" + w[1]
    			print (my_st, end=' ', file = out_file)
    		print(" ", file = out_file)
    	print(" ", file = out_file)
    
    #Write the vocabulary size of corpus to stdout.
    #to create a flat list of all sentences:
    sentences = []
    for x in data_sent:
    	for y in x:
        	sentences.append(y)
    
    words = [nltk.word_tokenize(sent) for sent in sentences]
    #to create a flat list of all words:
    all_words =[]
    for s in words:
    	for w in s:
    		all_words.append(w)
    #to lower case:
    flat_words = [word.lower() for word in all_words]
    print("The vocabulary size is ", end = "")   
    print(len(set(flat_words)))
    
    #Write the most frequent part-of-speech tag and its frequency to the stdout.
    part_of_speech = nltk.pos_tag(all_words)
    tag_fd = nltk.FreqDist(tag for (word, tag) in part_of_speech)
    print("The most frequent part-of-speech tags is: ", end ="")
    print(tag_fd.most_common()[0][0], end = " ")
    print("with frequency ", end ="")
    print(tag_fd.most_common()[0][1])
    
    #Find the frequency of each unique word (after lowercasing) using the FreqDist module 
    #and write the list in decreasing order to a file named CORPUS NAME-word-freq.txt.
    word_fd = nltk.FreqDist(w for w in flat_words)
    file2_name = corpus_name + "-word-freq.txt"
    out_file2 = open(file2_name, 'w')
    #print (word_fd.most_common(), file = out_file2)
    for w in word_fd.most_common():
    	print(repr(w[0]) + "/" + repr(w[1]), file = out_file2)
    
    #Find the frequency of each word given it’s part-of-speech tag. Use a conditional 
    #frequency distribution for this (ConditionalFreqDist) where the first item in 
    #the pair is the part-of-speech and the second item is the lowercased word. Note, 
    #the part-of-speech tagger requires uppercase words and returns the word/tag pair in 
    #the inverse order of what we are asking here. Use the tabulate() method of 
    #the ConditionalFreqDist class to write the results to a file named CORPUS NAME-pos-word-freq.txt.
    vocabulary = sorted(set(flat_words))
    file3_name = corpus_name + "-pos-word-freq.txt"
    out_file3 = open(file3_name, 'w')
    
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in part_of_speech)
    #print a table    
    print ("    ", end=" ", file = out_file3)
    for w in vocabulary:
    	print(w.rjust(15), end= " ", file = out_file3)
    print(" ", file = out_file3)
    for pos in cfd.conditions():
    	word_freq_dist_for_pos = cfd[pos]
    	print (pos.rjust(4), end=" ", file = out_file3)
    	for word in vocabulary:
    		num_times_word_was_pos = word_freq_dist_for_pos.get(word, 0)
    		print (repr(num_times_word_was_pos).rjust(15), end=" ", file = out_file3)
    	print(" ", file = out_file3)
 
    #For the most frequent word in the NN (nouns), VBD (past-tense verbs), JJ (adjectives)
    # and RB (adjectives) part-of-speech tags, find the most similar words using
    # Text.similar(). Write the output to stdout (this will happen by default).
    text = nltk.Text(flat_words)

    word_freq_dist_for_pos_NN = cfd["NN"]

    print("The most frequent noun (NN) is ", end ="")
    w1 = word_freq_dist_for_pos_NN.most_common()[0][0]
    print(w1)
    print("The similar words: ")
    text.similar(w1)
    
    word_freq_dist_for_pos_VBD = cfd["VBD"]
    print("The most frequent past-tense verb (VBD) is ", end ="")
    w2 = word_freq_dist_for_pos_VBD.most_common()[0][0]
    print(w2)
    print("The similar words: ")
    text.similar(w2)
    
    word_freq_dist_for_pos_JJ = cfd["JJ"]
    print("The most frequent adjective (JJ) is ", end ="")
    w3 = word_freq_dist_for_pos_JJ.most_common()[0][0]
    print(w3)
    print("The similar words: ")
    text.similar(w3)
    
    word_freq_dist_for_pos_RB = cfd["RB"]
    print("The most frequent adverbs (RB) is ", end ="")
    w4 = word_freq_dist_for_pos_RB.most_common()[0][0]
    print(w4)
    print("The similar words: ")
    text.similar(w4)
    
    #Write the collocations to the stdout.
    print("The collocations:")
    text.collocations()
    
    #output:
    """
    The courpus name is fables
	The number of words in the corpus is 3766
	The vocabulary size is 918
	The most frequent part-of-speech tags is: NN with frequency 428
	The most frequent noun (NN) is sheep
	The similar words: 
	lion air serpent village lamb rest monkey grievance donkey peg
	sheepskin long while mutton husband man shadow cottager hare horn
	The most frequent past-tense verb (VBD) is was
	The similar words: 

	The most frequent adjective (JJ) is little
	The similar words: 

	The most frequent adverbs (RB) is so
	The similar words: 
	all suiting with killed saw at grabbed found imagining ruled when as
	caught
	The collocations:
	n't know; never yet; one day; hit upon; much better; went away

    """
        