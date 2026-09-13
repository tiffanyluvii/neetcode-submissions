class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for (String str: strs){
            result += str.length() + "#" + str;
        }

        return result;
    }

    public List<String> decode(String str) {
        int start = 0;
        int end; 
        List<String> strs = new ArrayList<String>();

        if (str == null || str.isEmpty()){
            return strs;
        }

        while (start < str.length()){
            end = start;
            while (str.charAt(end) != '#'){
                end++;
            }

            int length = Integer.parseInt(str.substring(start,end));
            start = end + 1;
            end = start + length;
            strs.add(str.substring(start,end));
            start = end;
        }

        return strs;
    }
}
