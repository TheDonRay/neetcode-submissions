from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    #base cases 
    if (len(my_dict) == 0): 
        return {} 

    if (len(keys) == 0): 
        return {} 

    final_dictionary = {} 

    for key in my_dict: 
        if (key not in keys): 
            #insert the value here as such 
            final_dictionary[key] = my_dict[key] 

    return final_dictionary
    



# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
