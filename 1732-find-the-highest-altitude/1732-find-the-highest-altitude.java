class Solution {
    public int largestAltitude(int[] gain) {
        int maxAlt = 0;
        int[] alts = new int[gain.length + 1];
        alts[0] = 0;
        int sum = 0;
        
        for (int i = 1; i < alts.length; i++) {
            sum += gain[i - 1];
            alts[i] = sum;
            
            if (sum > maxAlt) {
                maxAlt = sum;
            }
        }
        
        return maxAlt;
    }
}