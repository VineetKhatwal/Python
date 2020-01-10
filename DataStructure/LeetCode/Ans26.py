class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict ={}
        for i in nums:
            dict[i] = i
            
        nums.clear()
        
        for i in dict.keys():
            nums.append(i)
        nums.sort()
 
        return(len(nums))
        
