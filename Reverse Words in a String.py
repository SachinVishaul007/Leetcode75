class Solution:
    def reverseWords(self, s: str) -> str:
        clean_str = s.strip()
        words = clean_str.split()         # splits using >=1 whitespaces

        words.reverse()
        return " ".join(words)