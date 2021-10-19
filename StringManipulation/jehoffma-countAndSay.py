class Solution(object):
    def countAndSayRecursive(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        else:
            r = self.countAndSay(n-1)
            result = ""

            count = 1
            num = r[0]

            for i in range(1, len(r)):
                if r[i] == num:
                    count += 1
                else:
                    result += str(count) + num
                    num = r[i]
                    count = 1
            result += str(count) + num

            return result

    def countAndSayIterative(self, n):
        """
        :type n: int
        :rtype: str
        """

        x = 1
        result = "1"

        while x < n:
            newResult = ""

            c = 1
            num = result[0]
            for i in range(1, len(result)):
                if result[i] == num:
                    c += 1
                else:
                    newResult += str(c) + num
                    c = 1
                    num = result[i]
            newResult += str(c) + num

            result = newResult
            newResult = ""
            x += 1

        return result
