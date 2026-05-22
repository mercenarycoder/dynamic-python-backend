class Solution():
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #planning to use dictionary over here as a hashmap to track
        need = dict.fromkeys(t, 0)
        given = {}
        ansN = [-1, -1]
        anslen = float("infinity")
        left = 0
        have = 0
        neededL = len(t)
        
        for right in range(0, len(s)):
            c = s[right]
            given[c] = 1 + given.get(c, 0)
            
            if c in need and given[c] == need[c]:
                have += 1
            
            while have == neededL:
                if (right - left + 1) < anslen:
                    ansN = [left, right]
                    anslen = right - left + 1
                given[s[left]] -= 1
                
                if s[left] in need and given[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        print(ansN)
        print(s[ansN[0] : ansN[1]])
        return s[ansN[0] : ansN[1]] if anslen != float("infinity") else ""


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
