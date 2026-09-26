# First Bad Version

## 1. Problem
There are n versions of a product. One of them is bad, and it makes all the versions after it bad too. Using the provided isBadVersion API, I need to find the very first bad version

## 2. Approach
This is basically binary search again because the sequence of versions looks something like [False, False, True, True, True]. 
I set star to 1 and end to n. In the loop, I check the middle version.
IfisBadVersion(mid) is True, it means the first bad version is either this one or somewhere to the left, so I update end = mid. If it returns False, the version is good, meaning the first bad one has to be on the right, so I update start = mid + 1. The loop stops when start and end point to the same version

## 3. Time Complexity
**Time Complexity: O(log n)**
I divide the search space by 2 each time I call the API. So the maximum number of API calls is log2(n)

## 4. Space Complexity
**Space Complexity: O(1)**
I didn't use any extra memory, just the start, end, and mid variables to keep track of the indices

## 5. Reflection / Improvement
The brute force solution would be calling the API starting from version 1 until it returns True, which would take O(n) calls in the worst case. The binary search method is already O(log n), so it is optimal and doesn't really need further improvement