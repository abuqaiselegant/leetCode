class Solution {
    public int lengthOfLastWord(String s) {
      //  String[] words = s.split("\\s");
        // String lastWord = words[words.length-1];
        // int count=0;
        // for(int i=0;i<lastWord.length();i++){
        //     count++;
        // }
        // return count;
        String[] sb = s.split(" ");
        return sb[sb.length-1].length();
    }
}