def searchRange(nums, target):

        list = []

        try:
            indexLow = nums.index(target)
        except ValueError:
            list = [-1,-1]
            return list
            
        
        list.append(indexLow)
            
        nums.reverse()

        indexHigh = nums.index(target)

        indexHigh = len(nums) - indexHigh -1

        if indexHigh != indexLow:
            list.append(indexHigh)

        return list
        
list1 = [5,7,7,8,8,10]
print(searchRange(list1,11))

        
