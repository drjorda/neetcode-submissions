class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList<Character> chars = new ArrayList<Character>();
        if(s.length() != t.length()){
            return false;
        }
        for(char a: s.toCharArray()){
            chars.add(a);
        }
        for(char b: t.toCharArray()){
            if(chars.contains(b)){
                chars.remove((Character) b);
            } else {
                return false;
            }
        }
        return true;

    }
}
