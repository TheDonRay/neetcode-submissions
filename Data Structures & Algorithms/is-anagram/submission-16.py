class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two base cases here as such 
        if (len(s) != len(t)): 
            return False 

        if (len(s) == 0 and len(t) == 0): 
            return True 

        # create my hash map here as such 
        my_hashTable = {} 

        for char in s: 
            # insert into the hash table and update the index value as such 
            my_hashTable[char] = my_hashTable.get(char, 0) + 1  

        #now we compare it with t for every character in t to see if that character value in also comparable in s as well 
        for char in t:   
            if (my_hashTable.get(char, 0) == 0): 
                return False 
            my_hashTable[char] -= 1  
        
        return True


        
