class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> map  = new LinkedHashMap<>();
        for(int i = 0;i<s.length();i++){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1);
        }
        char a = 0;
        for (Map.Entry<Character,Integer> entry:map.entrySet()){
            if (entry.getValue().equals(1)){
                a = entry.getKey();
                break;
            }
        }
        for (int i = 0;i<s.length();i++){
            if (s.charAt(i)==a){
                return i;
            }
        }
        return -1;
    }
}