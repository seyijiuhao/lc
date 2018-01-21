class Solution :
    def TwoSum(self,nums,target):
        length = len(nums)
        for index in range(length) :
            for n in range(length-1,index):
                if(nums[index] + nums[n] == target):
                    return (index,n)
