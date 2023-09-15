class Solution {
    public boolean isPalindrome(String s) {        
        // initialize left and right pointers
        int l = 0;
        int r = s.length() - 1;
        
        while (l <= r) {
            char lC = s.charAt(l);
            char rC = s.charAt(r);
            
            if (!Character.isLetterOrDigit(lC)) {
                l++;
            } else if (!Character.isLetterOrDigit(rC)) {
                r--;
            } else if (Character.toLowerCase(lC) != Character.toLowerCase(rC)) {
                return false;
            } else {
                l++;
                r--;
            }
        }
        
        return true;
    }
}