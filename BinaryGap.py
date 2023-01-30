class Solution:
    def binarySearch(self, A, x):
        n = len(A)
        left, right = 0, n-1
        ans = -1
        while left <= right:
            mid = (left + right) /2
            if A[mid] <= x:
                left = mid+1
                ans = mid
            else:
                right = mid-1
        return ans