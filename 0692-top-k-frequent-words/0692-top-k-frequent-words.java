class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counter = new HashMap<>();
        
        for (String w : words) {
            counter.put(w, counter.getOrDefault(w, 0) + 1);
        }
        
        Queue<Map.Entry<String, Integer>> maxHeap = 
            new PriorityQueue<>((a, b) -> a.getValue().equals(b.getValue()) ? 
                                a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
        
        for (Map.Entry<String, Integer> e : counter.entrySet()) {
            maxHeap.add(e);
        }
        
        List<String> res = new ArrayList<>();
        while (k > 0) {
            res.add(maxHeap.poll().getKey());
            k--;
        }
        
        return res;
    }
}