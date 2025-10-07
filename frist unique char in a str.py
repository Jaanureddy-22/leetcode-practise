class Solution(object):
    def firstUniqChar(self, s):
        # Step 1: Count frequency
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1  #if already present return char else 0. later +1 added

        # Step 2: Find first unique
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
