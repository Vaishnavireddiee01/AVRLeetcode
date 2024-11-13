from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target <= nums[m]:
                    h = m - 1  # Target is in the left half
                else:
                    l = m + 1  # Target is in the right half
            else:  # Right half is sorted
                if nums[h] >= target >= nums[m]:
                    l = m + 1  # Target is in the right half
                else:
                    h = m - 1  # Target is in the left half
        
        return -1  # If the target is not found


# Driver Code
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums = [15, 18, 19, 2, 3, 6, 7]
    target = 3
    result = solution.search(nums, target)
    print(f"Index of target {target}: {result}")  # Expected output: 4
    
    # Test case 2
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = solution.search(nums, target)
    print(f"Index of target {target}: {result}")  # Expected output: 4
    
    # Test case 3
    nums = [1, 3]
    target = 3
    result = solution.search(nums, target)
    print(f"Index of target {target}: {result}")  # Expected output: 1
    
    # Test case 4 (target not found)
    nums = [5, 6, 7, 9, 10, 1, 2]
    target = 8
    result = solution.search(nums, target)
    print(f"Index of target {target}: {result}")  # Expected output: -1
