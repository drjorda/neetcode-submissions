class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        ArrayList<int[]> counts = new ArrayList<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[(int) c - (int) 'a']++;
            }
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
