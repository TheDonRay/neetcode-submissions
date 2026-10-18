class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #start of with a base case here as such 
        if (len(s) != len(t)): 
            return False 

        if (len(s) == 0 and len(t) == 0): 
            return True 
        
        #create a hashmap 
        my_hash = {} 

        for char in s: 
            my_hash[char] = my_hash.get(char, 0) + 1 
            
        for char in t: 
            if (my_hash.get(char, 0) == 0): 
                return False 
            my_hash[char] -= 1 
        
        return True 