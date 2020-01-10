class Solution:
    def removeElement(self, nums, val):
        
        list = []
        temp = nums.copy() #  Deep Copy 
        nums.clear()    # temp = copy will delete temp after nums.copy()

        for i in temp:
            if i != val:
                nums.append(i)
    
        return(len(nums))
        
