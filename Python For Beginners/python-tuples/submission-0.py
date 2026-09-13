from typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:
    #create a empty tuple here as such 
    empty_tuple = () 
    adding_pair = (name, age) 
    #we can concatenate them here as such 
    return empty_tuple + adding_pair 

# do not modify code below this line
print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))
