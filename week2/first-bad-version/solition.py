class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                # The first bad one is either this mid or before it
                end = mid
            else:  
                # The first bad one is after mid
                start = mid + 1 
        return start