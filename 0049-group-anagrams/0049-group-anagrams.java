class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> count = new HashMap<>();
        
        for (String s : strs) {
            // sort s
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted = String.valueOf(chars);
            
            if (!count.containsKey(sorted)) {
                count.put(sorted, new ArrayList<>());
            }
            
            count.get(sorted).add(s);
        }
        
        return new ArrayList<>(count.values());
    }
}