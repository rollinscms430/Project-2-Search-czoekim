# Word Ladder
# CZK, CMS430 

f = open('words.txt')
all_words = {}

def create_dict(dictionary, start_word):
    """Filters words from file based on length of start word"""
    values = [start_word]
    for each in dictionary:
        if (len(start_word)+1) == len(each):
            each = each.strip()
            all_words[each] = 0
            
    return all_words
    
all_words = create_dict(f, 'snakes')

def create_level(dictionary, exploring_word):
    """Creates level that consists of words in dictionary differing in only one 
    letter from the base word"""
        
    level_words = []
    
    for i in range(len(exploring_word)):
        first_half = exploring_word[:i]
        sec_half = exploring_word[i+1:]
        for j in 'abcdefghijklmnopqrstuvwxyz':
            if exploring_word[i] != j:
                new_word = first_half + j + sec_half
                if new_word in dictionary:
                    level_words.append(new_word)
    
    return level_words


def find_end(dictionary, start_word, end_word):
    """ Finds the shortest path from start_word to end_word using
    breadth-first-search """
    
    memory = {}
    explored = []
    answer = [end_word]
    frontier = []
    queue = []
    queue.append((start_word, 1))
    
    while queue: #while frontier is not empty
    
        current = queue.pop(0)
        current_word = current[0]
        current_level = current[1] 
        
        """ Once end_word is found, searches memory dictionary to find direct
        parent node of the current word and appends it answer list.
        
        Current word becomes the parent and level decrements by 1. 
        Loop continues until level reaches 1 (start_word). """ 
        
        if current_word == end_word:
            while(current_level > 1):
                parent = memory[current_word]
                answer.append(parent)
                current_word = parent
                current_level = current_level-1
            return answer
        
        #Expands current word and adds it to the explored list
        new_level = create_level(dictionary, current_word)
        explored.append(current_word)
        
        #Adds each new word in level to frontier
        #Keeps record of direct parent (aka current_word) in memory
        #Pushes new word onto back of queue
        for new_word in new_level:
            if new_word not in explored and new_word not in frontier:
                frontier.append(new_word)
                memory[new_word] = current_word
                queue.append((new_word, current_level+1))
                
print find_end(all_words, 'snakes', 'brains')
            

    