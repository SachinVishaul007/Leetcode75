# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         s=""
#         i=0
#         j=0

#         while(i<len(word1) and j<len(word2)):
#             s+=word1[i]
#             i+=1
#             s+=word2[j]
#             j+=1

#         while(i<len(word1)):
#             s+=word1[i]
#             i+=1
        
#         while(j<len(word2)):
#             s+=word2[j]
#             j+=1

#         return s

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        p =0
        while(p<len(word1) and p<len(word2) ):
            res.append(word1[p])
            res.append(word2[p])
            p+=1

        if(p>=len(word1)):
            res+= word2[p:]
        else:
            res+= word1[p:]
                
        

        return "".join(res)