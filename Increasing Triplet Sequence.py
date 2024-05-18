#Extremely tough Optimal solution O(1) space O(n)Time
# f,s,t stand for first, second and third element. But note that they don't record the first second and third element always in order, this technique is used to simply find if there exists an order
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')

        for t in nums:
            if(t<=f):
                f=t
            elif(t<=s):
                s=t
            else:
                return True
        return False

# O(n) Space O(n) Time Complexity
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         min_val = float('inf')
#         max_val = float('-inf')

#         min_arr = []
#         for n in nums:
#             if(n> min_val):
#                 min_arr.append(True)
#             else:
#                 min_arr.append(False)

#             min_val = min(min_val, n)
            
#         max_arr = []
#         for i in range(len(nums)-1,-1,-1):
#             if(nums[i]<max_val):
#                 max_arr.append(True)
#             else:
#                 max_arr.append(False)
#             max_val = max(max_val, nums[i])
        
#         max_arr.reverse()

#         print(min_arr)
        
#         print(max_arr)
#         for x,y in zip(min_arr,max_arr):
#             if x and y:
#                 return True

    
#         return False




# There should always be a Brute force solution, there should have been a brute force O(n^3) for this 