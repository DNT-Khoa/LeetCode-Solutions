class Solution { 
    public List<List<Integer>> threeSum(int[] nums) {
        // First sort array
        Arrays.sort(nums);
        
        // return list
        List<List<Integer>> res = new ArrayList<>();
        
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            int target = -nums[i];
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int total = nums[left] + nums[right];
                if (total < target) {
                    left++;
                } else if (total > target) {
                    right--;
                } else {
                    List<Integer> triplet = new ArrayList<>(List.of(nums[i], nums[left], nums[right]));
                    res.add(triplet);
                    
                    // skip duplicated upcoming nums at left and right pointers
                    while (left < right && nums[left] == triplet.get(1)) {
                        left++;
                    }
                    
                    while (left < right && nums[right] == triplet.get(2)) {
                        right--;
                    }
                }
            }
            
            while (i + 1 < n && nums[i] == nums[i + 1]) {
                i++;
            }
        }
        
        
        
        return res;
    }
}