def concatenate(s1: str, s2: str) -> str:
    combined_string = s1 + s2   
    # before i had the logic flipped but fixed it here
    if (len(combined_string) > 10): 
        return "Too long!"
    return combined_string 
    


# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
