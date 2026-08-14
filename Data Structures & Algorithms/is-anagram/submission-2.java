class Solution {
    public HashMap<Character, Integer> getMap(String s){
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c: s.toCharArray()){
            map.put((Character)c, (map.getOrDefault((Character)c, 0) + 1));
        }
        return map;
    }
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = getMap(s);
        HashMap<Character, Integer> tMap = getMap(t);
        return sMap.equals(tMap);
    }
}
