class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        length = 0
        is_odd = False
        for i in s:
            count[i] = 1 + count.get(i, 0)
        for c in count.values():
            if c%2 == 0:
                length += c
            else:
                is_odd = True
                length += c - 1
        
        if is_odd:
            length += 1
        return length
        