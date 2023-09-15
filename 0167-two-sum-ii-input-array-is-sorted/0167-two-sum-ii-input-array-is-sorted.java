class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int left = 0;
        int right = n - 1;
        int[] res = new int[2];
        
        while (left < right) {
            int total = numbers[left] + numbers[right];
            if (total > target) {
                right--;
            } else if (total < target) {
                left++;
            } else {
                res[0] = left + 1;
                res[1] = right + 1;
                break;
            }
        }
        
        return res;
    }
}