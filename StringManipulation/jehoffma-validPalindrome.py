class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
        left = 0
        right = len(s)-1
        s = s.lower()

        while left < right:
            if s[left] not in alpha:
                left += 1
            elif s[right] not in alpha:
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
