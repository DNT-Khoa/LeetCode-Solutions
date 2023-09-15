class Solution {
    public boolean isPalindrome(String s) {        
        // remove all spaces and lowercase string
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int n = s.length();
        
        if (n == 1) return true;
        
        // initialize left and right pointers
        int l = 0;
        int r = n - 1;
        
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            
            l++;
            r--;
        }
        
        return true;
    }
}