class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        list_3sum = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range (j+1, len(nums)):
                    list =[]
                    if nums[i]+nums[j]+nums[k] == 0:
                        list.append(nums[i])
                        list.append(nums[j])
                        list.append(nums[k])
                        
                    if list not in list_3sum and list:
                        list_3sum.append(list)

                    
        print(list_3sum)      
        return list_3sum
                    
        
