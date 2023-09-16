class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int len = numbers.length;
        int lPointer = 0;
        int rPointer = len - 1;
        
        int[] res = new int[2];
        
        while (lPointer != rPointer) {
            int total = numbers[lPointer] + numbers[rPointer];
            
            if (total < target) {
                lPointer++;
            } else if (total > target) {
                rPointer--;
            } else {
                res[0] = lPointer + 1;
                res[1] = rPointer + 1;
                break;
            }
        }
        
        return res;
    }
}