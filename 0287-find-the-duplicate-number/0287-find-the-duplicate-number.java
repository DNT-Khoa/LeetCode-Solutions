class Solution {
    public int findDuplicate(int[] nums) {
        int lPointer = 0;
        int rPointer = 0;
        
        // Use Floyd cycle detection algorithms
        // 1. Find the intersection points for slow and fast pointers
        while (true) {
            lPointer = nums[lPointer]; // left pointer moves 1 node at a time
            rPointer = nums[nums[rPointer]]; // right pointer moves twice the speed of left pointer
            
            if (lPointer == rPointer) break;
        }
        
        // 2. Find the start of the cycle, which is also the repeat number
        // 2.1 Move the rPointer to the first node
        lPointer = 0;
        // 2.2 Move left and right pointers one node at a time, until they meet each other
        // the point where they meet is also the repeat number
        while (lPointer != rPointer) {
            lPointer = nums[lPointer];
            rPointer = nums[rPointer];
        }
        
        return lPointer;
    }
}