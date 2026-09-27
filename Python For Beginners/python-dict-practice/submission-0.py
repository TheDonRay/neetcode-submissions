from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    # first let us check if the word exists 
    if (len(word) == 0): 
        return {} 
    
    #initialize a empty dictionary here 
    my_dictionary = {}  

    for ch in word: 
        if (ch in my_dictionary): 
            my_dictionary[ch] += 1 
        else: 
            my_dictionary[ch] = 1

    return my_dictionary





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
