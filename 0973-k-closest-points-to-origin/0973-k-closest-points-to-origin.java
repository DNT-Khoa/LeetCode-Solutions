class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> minHeap = new PriorityQueue<>((a, b) -> (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]));
        
        for (int[] point : points) {
            minHeap.add(point);
        }
        
        int[][] res = new int[k][2];
        
        while (k > 0) {
            res[--k] = minHeap.poll();
        }
        
        return res;
    }
}