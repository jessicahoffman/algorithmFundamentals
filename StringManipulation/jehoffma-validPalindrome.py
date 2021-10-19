class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
        left = 0
        right = len(s)-1
        read = 0
        s = string.lower(s)

        while(read < len(s)/2 and left < right):
            if s[left] not in alpha:
                left += 1
            elif s[right] not in alpha:
                right -= 1
            elif s[left] != s[right]:
                # print(s[left])
                # print(s[right])
                return False
            else:
                # print(s[left])
                # print(s[right])
                left += 1
                right -= 1
                read += 1
        return True
