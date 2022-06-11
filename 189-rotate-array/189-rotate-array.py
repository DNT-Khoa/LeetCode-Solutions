class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        nums[:] = nums[n-k:n] + nums[0:n-k]
        
        
# Time complexity O(n)