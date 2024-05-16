class Solution:
    def isVowel(self, char):                                      # Easy vowel check in python
        vowels = 'aeiouAEIOU'
        return char in vowels

    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s_list = list(s)
        while (l<r):
            while(l<len(s) and  not(self.isVowel(s[l]))):
                l+=1

            while(r>=0 and  not(self.isVowel(s[r]))):
                r-=1

            if l<r:
                s_list[l] , s_list[r] =  s_list[r] , s_list[l]             #Swapping in python
                l+=1
                r-=1


            
        return "".join(s_list)

        