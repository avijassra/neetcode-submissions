public class Solution {
    public bool IsPalindrome(string s) {
        var l = 0;
        var r = s.ToCharArray().Length-1;

        while (l < r) {
            if (!char.IsLetterOrDigit(s[l])) {
                l += 1;
                continue;
            }
            if (!char.IsLetterOrDigit(s[r])) {
                r -= 1;
                continue;
            }
            if (char.ToUpper(s[l]) == char.ToUpper(s[r])) {
                l += 1;
                r -= 1;
            } else {
                return false;
            }
        }

        return true;
    }
}
