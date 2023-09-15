import java.util.Collections;

class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int n = nums.size();
        if (n == 1) {
            return 0;
        }
        
        // Sort the list => O(nlogn)
        Collections.sort(nums);
        
        int left = 0, right = n - 1;
        int counter = 0;
        
        while (left < right) {
            int total = nums.get(left) + nums.get(right);
            if (total >= target) {
                right--;
            } else {
                counter += right - left;
                left++;
            }
        }
        
        return counter;
    }
}