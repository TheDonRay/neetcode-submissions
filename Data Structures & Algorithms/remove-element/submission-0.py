class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # goal of this problem here 
        # remove all occurences of val from the array 
        # order may be changed  
        # first thing we need to handle is the removal of elements from the list 

        #base case 
        if (len(nums) == 0): 
            return 0 

        #still need to learn two pointers 

        temp_array = [] 
        for number in nums: 
            if (number != val):  
                temp_array.append(number) 
            else:  
                continue  
        
        #now we need to add those values into nums and replace them 
        for i in range(len(temp_array)): 
            nums[i] = temp_array[i] 
        return len(temp_array)