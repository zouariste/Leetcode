class Solution(object):
    def minPartitions(self, n):
        for elt in range(9, 0, -1):
            if str(elt) in n:
                return elt
        return 0
