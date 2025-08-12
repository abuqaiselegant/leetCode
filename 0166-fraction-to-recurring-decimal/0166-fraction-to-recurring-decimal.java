class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuilder sb = new StringBuilder();
        if (numerator==0){
            return "0";
        }
        if (numerator<0 ^ denominator<0){
            sb.append("-");
        }
        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);
        
        Map<Long, Integer> seen = new HashMap<>();
        long x = num/den;
        sb.append(x);
        long y = num%den;
        if (y!=0){
            sb.append(".");
        }
        while(y!=0){
            
            if (seen.containsKey(y)){
                int pos = seen.get(y);
                sb.insert(pos,"(");
                sb.append(")");
                break;
            }
            seen.put(y,sb.length());

            y *=10;
            long digit = y/den;
            sb.append(digit);
            y%=den;

        }
        return sb.toString();
    }
}