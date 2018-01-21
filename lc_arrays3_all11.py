class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #从右向左检索第一个比heigt[i]大的height[j]，若大于maxsize则存为maxsize
        maxsize=0
        for i in range(0,len(height)):
            for j in range(len(height)-1,-1,-1):
                if(height[j]>height[i] and maxsize<abs(j-i)*height[i]):
                    maxsize=abs(j-i)*height[i]
                    break
        return maxsize
    #左右指针分别指向头尾，求得此时maxsize，再比较左右指针指向值大小，若左大有指针移动，若右大左指针移动移动
    def MAXArea(self,height):
        maxsize=0
        i=0
        j=len(height)-1
        while(i<j):
            maxsize=max(maxsize,(j-i)*min(height[i],height[j]))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxsize
li_h=[1,2,3,4,5,6,7,8,9,10]
obj=Solution()
size=obj.MAXArea(li_h)
print(size)
