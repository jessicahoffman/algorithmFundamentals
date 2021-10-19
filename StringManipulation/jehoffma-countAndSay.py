class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if (n == 1):
            return "1"
        else:
            prev = self.countAndSay(n-1)
            new = ""

            x = prev[0]
            count = 0
            for char in prev:
                if (x == char):
                    count += 1
                else:
                    new += str(count) + x
                    x = char
                    count = 1

            new += str(count) + x
            return new
