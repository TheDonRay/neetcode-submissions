def get_substring(input_string: str, start: int, end: int) -> str:
    #get the length first to check if its valid params  
    len_of_string = len(input_string) 
    if (len_of_string < end): 
        return " " 
    
    get_substring = input_string[start:end]
    return get_substring 
    



# do not modify below this line
print(get_substring("NeetCode", 1, 7))
print(get_substring("NeetCode", 1, 8))
print(get_substring("NeetCode", 1, 9))
print(get_substring("NeetCode", 0, 2))
print(get_substring("NeetCode", 0, 7))
print(get_substring("NeetCode", 4, 8))
