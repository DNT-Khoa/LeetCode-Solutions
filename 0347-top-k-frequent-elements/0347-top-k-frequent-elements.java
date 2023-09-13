import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        
        // Count occurences of numbers and save them in a hashmap
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        // Create a bucket
        List<Integer>[] bucket = new ArrayList[nums.length + 1];

        // Fill the bucket
        for (int key : count.keySet()) {
            int frequency = count.get(key);

            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }
    
        List<Integer> res = new ArrayList<>();

        for (int pos = bucket.length - 1; pos > 0 && res.size() < k; pos--) {
            if (bucket[pos] != null) {
                res.addAll(bucket[pos]);
            }
        }

        return res.subList(0, k).stream().mapToInt(i -> i).toArray();
    }
}