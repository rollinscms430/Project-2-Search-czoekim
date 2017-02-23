# Anagrams 
# CZK, CMS430

f= open('words.txt')

d = {}

for word in f:
    
    #Takes all words in file and sorts them in alphabetical order
    word = word.strip()
    word_list = [] #value for dict
    sorted_word = tuple(sorted(word)) #key for dict
    
    #Checks if sorted word is already a key in dict
    #If so, adds original word to list at key's value
    #If not, creates a new key
    if sorted_word not in d:
        word_list.append(word)
        d[sorted_word] = word_list
    else:
        d[sorted_word].append(word)

    #Checks for all lists in dict that has at least a pair of words
for list in d:
    if len(d[list]) > 1:
        print d[list]



