class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # start of with base case here as such 
        if (len(nums) == 0): 
            return 0 


        # create two counters here as such 
        # one for keeping track of current streak 
        # another for max streak 

        currentStreak = 0 
        max_streak = 0 

        for numbers in nums: 
            if (numbers == 1): 
                currentStreak += 1  
                # keep track of that by updating the max streak to have the max streak 
                max_streak = max(currentStreak, max_streak)  
            else: 
                # reset the current streak 
                currentStreak = 0 
        
        return max_streak