class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp= ""
        if(len(str1)<len(str2)):
            temp = str1
        else:
            temp = str2
        while(len(temp)>0):
            if(self.isDiv(str1, temp) and self.isDiv(str2,temp)):
                return temp
            temp = temp[:-1]
        return ""
        
    def isDiv(self, big_str: str, div:str) -> bool:
        k=0
        if(len(big_str)%len(div)!=0):
            return False
        for i in range(0, len(big_str)):
            k = i%len(div)
            if big_str[i]!=div[k]:
                return False
            
        return True
