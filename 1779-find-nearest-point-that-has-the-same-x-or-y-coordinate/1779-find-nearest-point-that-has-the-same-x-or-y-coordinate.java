class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int minIndex = -1;
        int minVal = Integer.MAX_VALUE;
        
        for (int i = 0; i < points.length; i++) {
            int[] point = points[i];
            if (point[0] == x || point[1] == y) {
                int md = Math.abs(point[0] - x) + Math.abs(point[1] - y);
                
                if (md < minVal) {
                    minIndex = i;
                    minVal = md;
                }
            }
        }
        
        return minIndex;
    }
}
