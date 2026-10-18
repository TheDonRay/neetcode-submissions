class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #start of with a base case here as such 
        if (len(nums) == 0 and target == 0): 
            return [] 

        solution_array = [] 

        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                if (nums[i] + nums[j] == target): 
                    # we want to add that index into the solution array 
                    solution_array.append(i) 
                    solution_array.append(j) 
        
        return solution_array