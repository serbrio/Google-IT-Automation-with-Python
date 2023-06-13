#!/usr/bin/python
# -*- coding: utf-8 -*-

import wordcloud
from matplotlib import pyplot as plt
import sys


def get_file_contents(filename):
    with open(filename, encoding="utf-8", errors='ignore') as file:
        file_contents = file.read()
    #print(file_contents.encode('utf-8'))
    return file_contents    



#Task is: 
#Write a function that iterates through the words in file_contents, 
#removes punctuation, and counts the frequency of each word. 
#Oh, and be sure to make it ignore word case, 
#words that do not contain all alphabets 
#and boring words like "and" or "the". 
#Then use it in the generate_from_frequencies function 
#to generate your very own word cloud!
#Hint: Try storing the results of your iteration in a dictionary 
#before passing them into wordcloud via the generate_from_frequencies function.

def calculate_frequencies(file_contents, max_words):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "on", "up", "so", "got", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her","hers", "its", "they", "them", "not", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "then", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "than", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "in", "for"]
    
    # LEARNER CODE STARTS HERE
    result = {}
    for word in file_contents.split():
        stripped_word = word.lower().strip(punctuations)
        if stripped_word.isalpha() and stripped_word not in uninteresting_words:
            if stripped_word not in result:
                result[stripped_word] = 0
            else:
                result[stripped_word] += 1
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])[-max_words:]}
    for key, value in sorted_result.items():
        print("{}: {}".format(key.encode("utf-8"), value))

    #wordcloud
    cloud = wordcloud.WordCloud(width=1600, height=800, max_words=max_words)
    cloud.generate_from_frequencies(result)
    return cloud.to_array()
    
    
# Display your wordcloud image
filename = sys.argv[1]
file_contents = get_file_contents(filename)
myimage = calculate_frequencies(file_contents, 50)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()