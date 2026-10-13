class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #base case here as such 
        if (len(nums) == 0):
            return False  

        seen_set = set() 

        for number in nums: 
            if (number in seen_set): 
                return True 
            seen_set.add(number) 
            
        return False