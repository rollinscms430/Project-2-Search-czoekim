# Anagrams 
# CZK, CMS430

f= open('words.txt')

d = {}

for word in f:
    word = word.strip()
    word_list = [] #value for dict
    sorted_word = tuple(sorted(word)) #key for dict
    
    if sorted_word not in d:
        word_list.append(word)
        d[sorted_word] = word_list
    else:
        d[sorted_word].append(word)

for list in d:
    if len(d[list]) > 1:
        print d[list]



