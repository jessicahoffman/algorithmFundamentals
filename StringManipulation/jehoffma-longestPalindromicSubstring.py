class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        mid = len(s)//2

        sub = self.checkCenter(s, mid)
        shift = 1

        while len(sub)//2 + shift <= mid:
            for each in [shift, -shift]:
                nextt = self.checkCenter(s, mid + each)
                if len(nextt) > len(sub):
                    sub = nextt

            shift += 1
        return sub

    def checkCenter(self, s, c):
        even = None
        c2 = c + 1
        c -= 1

        if c2 >= len(s):
            even = True
            c2 -= 1

        while c >= 0 and c2 < len(s):
            if even == None and not s[c] == s[c+1]:
                even = False
            if not s[c] == s[c2]:

                if even == None and s[c] == s[c2-1]:
                    even = True
                    c2 -= 1
                else:
                    break
            if even == None and c2 == len(s)-1:
                if c > 0 and s[c2] == s[c-1]:
                    even = True
                    c2 -= 1

            c -= 1
            c2 += 1
        return s[c+1:c2]
