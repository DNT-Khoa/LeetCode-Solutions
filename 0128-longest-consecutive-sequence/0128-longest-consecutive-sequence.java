class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> mySet = new HashSet<>();
        int counter = 0;
        // add elements in nums to set
        for (int n : nums) {
            mySet.add(n);
        }
        
        for (int n : nums) {
            int temp = 0;
            
            if (!mySet.contains(n - 1)) {
                while (mySet.contains(n)) {
                    temp++;
                    if (temp > counter) {
                        counter = temp;
                    }
                    n++;
                }
            }
        }
        
        return counter;
    }
}