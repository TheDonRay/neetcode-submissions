class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #start of with a base case here as such 
        if (len(arr) == 0): 
            return [] 

        # we know that the right most value is -1 so we know that can be the max value to the right of the array either way 
        right_max = -1 
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i] # using this later
            arr[i] = right_max # already updated the element to the right_max value 
            right_max = max(current, right_max) 
                            #2          -1 = max = 2  

        return arr 
        
