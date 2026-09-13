from typing import List, Set 

def count_unique_words(words: List[str]) -> int:
    #base case here 
    if (len(words) == 0): 
        return 0 
    
    count = 0 

    #convert the list into a set here  
    #set contains unique elements only
    unique_set_of_words = set(words) 
    for word in unique_set_of_words: 
        count += 1

    return count 


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
