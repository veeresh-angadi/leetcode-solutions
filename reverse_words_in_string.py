class Solution:
    def reverseWords(self, s: str) -> str:
        s1=s.split()
        s1=s1[::-1]
        result=" ".join(s1)
        return result
