class Solution {
    public boolean checkValid(int[][] matrix) {
        int n = matrix[0].length;
        Set<String> check = new HashSet<>();
        
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int value = matrix[r][c];
                
                if (!check.add(value + " in row " + r)
                || !check.add(value + " in column " + c)
                || !(value >= 1 && value <= n)
                ) {
                    return false;
                }
            }
        }
        
        return true;
    }
}