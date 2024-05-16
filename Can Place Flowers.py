class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed)==1):
            if((flowerbed[0]==0 and n<=1) or (flowerbed[0]==1 and n==0)):
                return True
            else:
                return False
        for i in range(0,len(flowerbed)):
            if(not(i==0 or i==len(flowerbed)-1)):
                if(flowerbed[i]!=1 and (flowerbed[i-1]==0 and flowerbed[i+1] == 0)):
                    flowerbed[i]=1
                    n-=1
            elif(i==0):
                if(flowerbed[i]!=1 and flowerbed[1]==0):
                    flowerbed[0]=1
                    n-=1
            else:
                if(flowerbed[i]!=1 and flowerbed[i-1]==0):
                    flowerbed[i]=1
                    n-=1


        if(n>0):
            return False
        return True
    


    #  another optimal solution is by adding 0's on both sides of the list:

    # class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     s = len(flowerbed)
    #     bed = [0] + flowerbed + [0]
        
    #     for i in range(1, s+1):
    #         if bed[i] == bed[i-1] == bed[i+1] == 0:
    #             bed[i] = 1
    #             n -= 1
            
    #         if n <= 0: return True
        
    #     return False

