class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int n = nums.size();
        if (n == 1) {
            return 0;
        }
        
        int counter = 0;
        int left = 0, right = 1;
        
        while (left < n - 1) {
            int total = nums.get(left) + nums.get(right);
            
            if (total < target) {
                counter++;
            }
            
            right++;
            
             if (right == n) {
                left++;
                right = left + 1;
            }
        }
        
        return counter;
    }
}