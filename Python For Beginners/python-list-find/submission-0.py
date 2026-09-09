from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int: 
    index_found = 0
    for element in nums: 
        if element == target: 
            index_found = nums.index(element)  
        else: 
            continue 
    return index_found



# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

