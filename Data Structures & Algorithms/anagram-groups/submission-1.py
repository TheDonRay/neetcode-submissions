class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case here as such 
        if (len(strs) == 0): 
            return [[]] 
            
        # create my hashmap here as such 
        my_hashmap = {} 

        for string in strs: 
            #define a key here which is going to be the sorted version of the string as such         
            key = "".join(sorted(string)) 
            #if statement here to see if that value is seen in our hashmap if not we can just return an empty array value 
            if key not in my_hashmap: 
                # we assign it the empty array here as such 
                my_hashmap[key] = [] 
            #if it is its already an anagram 
            my_hashmap[key].append(string) 
        #finally return the values of all the key values in the hashmap here as such  
        return list(my_hashmap.values()) # going to return a single array so what I want to do is convert to a list to return a double array here as such. 
