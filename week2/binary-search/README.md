# Binary Search

## 1. Problem
I need to find a target number in a sorted array and return its index. If the number is not in the array, I should return -1

## 2. Approach
Since the array is already sorted, I can use binary search instead of checking every single element. I created two pointers,  for the start and r for the end of the array. Then I find the middle element. 
If my target is bigger than the middle element, I know it's not in the left half, so I move l to mid + 1. If it's smaller, I move r to mid - 1 to ignore the right half. I keep looping until l passes r

## 3. Time Complexity
**Time Complexity: O(log n)**
Because every time the loop runs, I cut the search area in half. This is much faster than checking every element, and the number of steps grows logarithmically with n

## 4. Space Complexity
**Space Complexity: O(1)**
I didn't create any new arrays or data structures. I only used a few integer variables (l, r, mid), so the memory used doesn't depend on the size of the input

## 5. Reflection / Improvement
This is already the best approach. If I used a simple for loop to check the whole array (brute-force), the time complexity would be O(n). By using binary search, I improved it to O(log n)