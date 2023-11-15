class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        
        for (int num : nums) {
            maxHeap.add(num);
        }
        
        int res = 0;
        
        while (k >= 1) {
            res = maxHeap.poll();
            k--;
        }
        
        return res;
    }
}