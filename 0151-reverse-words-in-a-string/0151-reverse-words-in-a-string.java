class Solution {
    public String reverseWords(String s) {
        String[] a = s.split(" ");
        String ans = "";

        for (int i = a.length - 1; i >= 0; i--) {
            if (!a[i].equals("")) {
                ans = ans + a[i] + " ";
            }
        }

        return ans.trim();
    }
}