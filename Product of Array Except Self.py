class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [] 
        mul=1

        for i in nums:
            mul*=i
            left.append(mul)

        right = []
        mul=1

        for num in reversed(nums):
            mul *= num
            right.append(mul)
        right = list(reversed(right))

        left = [1] + left + [1]
        right = [1] + right + [1]
        ans=[]
        for i in range(1,len(left)-1):
            ans.append(left[i-1] * right[i+1])

        return ans