from typing import List, Set 

def contains_duplicate(words: List[str]) -> bool:
    length_of_original = len(words) 
    unique_set = set(words) 
    # for word in words: 
    #     unique_set.add(word) 
    
    if (length_of_original == len(unique_set)): 
        return False 
    else: 
        return True 

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
