from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    #start of with empty list 
    my_array = [] 
    for name in age_dict: 
        my_array.append(name) 
    
    return my_array 


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    # start of by creating an empty list here as such 
    my_array = [] 
    for name in age_dict: 
        age_value = age_dict[name] 
        # add value to the array as such 
        my_array.append(age_value) 
    
    return my_array

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
