class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> a = new HashMap<String, Integer>();

        for (char character : s.toCharArray()){
            String charStr = character + "";
            if (!a.containsKey(charStr)){
                a.put(charStr, 1);
            } else {
                a.put(charStr, a.get(charStr) + 1);
            }
        }

        for (char character : t.toCharArray()){
            String charStr = character + "";
            if (!a.containsKey(charStr)){
                return false;
            } else {
                a.put(charStr, a.get(charStr) - 1);
                if (a.get(charStr) == 0){
                    a.remove(charStr);
                }
            }
        }

        

        return a.isEmpty();
    }
}
