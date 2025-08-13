class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> match = new HashMap<>();
        match.put(')', '(');
        match.put(']', '[');
        match.put('}', '{');

        Stack<Character> stack = new Stack<>();
        // Deque<Type> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()){
            if (c == '(' || c =='[' || c=='{'){
                stack.push(c);
            }
            else{
                if (stack.isEmpty()) return false;   
                if (stack.pop()!=match.get(c)){
                    return false;
                }
                

                }
            }
        return stack.isEmpty();
        }
        


    }
