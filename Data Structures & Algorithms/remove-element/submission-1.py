class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start of with a base case here 
        if (len(nums) == 0): 
            return 0 

        # approach is brute force so what im going to do is create a temp array here 
        temp_array = [] 

        # iterate through all the elements in the original array and if that element is not in the original array put it into temp array since temp array is going to have the elements that are not val 
        for numbers in nums: 
            if (numbers != val): 
                #insert it into the temp_array as such 
                temp_array.append(numbers) 
            else: 
                continue 
        
        # now that the values are in the temp array we need to add them back into the nums array for that specific index 
        for i in range(len(temp_array)): 
            nums[i] = temp_array[i] 
        
        return len(temp_array)