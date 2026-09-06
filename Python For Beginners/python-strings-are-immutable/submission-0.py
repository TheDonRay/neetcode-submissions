def remove_fourth_character(word: str) -> str:
    before_fifth = word[4:]   
    before_fourth = word[:3]
    return before_fourth + before_fifth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
