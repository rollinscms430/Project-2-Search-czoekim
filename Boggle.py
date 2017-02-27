# Boggle
# CZK, CMS430 

f = open('words.txt')

letters = [['u','n','t','h'], ['g','a','e','s'], 
    ['s','r','t','r'], ['h','m', 'i', 'a']] 
    
positions = [[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,1),(1,2),(1,3)],
    [(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,1),(3,2),(3,3)]]

def gen_dict(dictionary):
    all_words = {}
    for each in dictionary:
        each = each.strip()
        all_words[each] = 0
        
    return all_words

def gen_prefix_dict(dictionary):
    prefix_dict = {}
    for each in dictionary:
        each = each.strip()
        prefix = each[:2]
        if prefix in prefix_dict:
            prefix_dict[prefix].append(each)
        else:
            prefix_dict[prefix] = [each]
    return prefix_dict

def create_level(curr_position):
    """Generates a new level with possible letters to explore 
    param: tuple - current position on board
    return: list - all horizontal, vertical, and diagonal adjacent letters """
    
    n = 4 #represents NXN matrix
    new_level = []
        
    row = curr_position[0] 
    col = curr_position[1]
        
    if row > 0: #top
        new_level.append((row-1, col))
        if col > 0: #top left diagonal
            new_level.append((row-1,col-1))
        if col < n -1: #top right diagonal
            new_level.append((row-1,col+1))
                
    if row < n - 1: #bottom
        new_level.append((row+1,col))
        if col > 0: #bottom left diagonal
            new_level.append((row+1,col-1))
        if col < n - 1: #bottom right diagonal
            new_level.append((row+1,col+1))
                    
    if col > 0: #left
        new_level.append((row,col-1))
            
    if col < n - 1: #right
        new_level.append((row,col+1))
    
    return new_level

def possible_pos_dict(positions):
    """ Generates a dictionary of possible letters using create_level method 
    on each position on the board
    param: list of positions
    returns: dictionary with position as key and list of adjacent 
    positions as its values """
    
    possible_pos_dict = {}
    for position_list in positions:
        for position in position_list:
            pos = create_level(position)
            possible_pos_dict[position] = pos
    
    return possible_pos_dict

def create_matrix(letters, positions):
    """ Assigns each letter to a position for fast lookup
    param: two lists - letters and positions
    returns: dictionary with each position as key and the corresponding letter
    to value """
    
    pos_letter = {}
    
    for letter_list, position_list in zip(letters, positions):
        for letter, position in zip(letter_list, position_list):
            pos_letter[position] = letter
    
    return pos_letter

def find_words(start):
    """Generates all possible words from the starting point using
    depth-first-search/stack
    
    param: start location on board
    returns: list of words that can be generated from that position
    """
    
    words = []
    stack = [] 
    
    # Stack: list of tuples - each tuple holds a possible position, 
    # a list of the sequence, and the letters of the sequence + the letter at
    # the possible position
    # A tuple is created for each possible position
    
    for possible_pos in position_dict[start]: 
        stack.append((possible_pos, [start], board.get(start)))

    while stack:
        current, sequence, letters = stack.pop()
        current_letter = board.get(current)
        
        word = letters + current_letter
        
        if len(word) == 2:
            if word not in prefix_dict:
                continue
            else:
                possible_letters = position_dict[current]
                
                #New tuples added to the stack of possible positions from the
                #current word. Keeps track of current sequence to make sure
                #none of the possibilities will overlap
                stack.extend([(possible_pos, sequence + [current], word) 
                for possible_pos in possible_letters if possible_pos not in sequence])
                
        if word in all_words:
            words.append(word)
            
            possible_letters = position_dict[current]
            
            #In case words can be formed by a word already in dictionary
            stack.extend([(possible_pos, sequence + [current], word) 
            for possible_pos in possible_letters if possible_pos not in sequence])
        
    return words
    
all_words = gen_dict(f)  
prefix_dict = gen_prefix_dict(all_words)
board = create_matrix(letters, positions)
position_dict = possible_pos_dict(positions)

for position_list in positions:
    for position in position_list:
        print board.get(position), position, find_words(position), '\n'
