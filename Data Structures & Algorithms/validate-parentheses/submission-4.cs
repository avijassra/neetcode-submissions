public class Solution {
    public bool IsValid(string s) {
        var res = true;
        var stack = new Stack<char>();
        var tags = new Dictionary<char, char>(){
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };

        foreach (char c in s) {
            if(tags.ContainsKey(c)) {
                stack.Push(tags[c]);
            } else if(stack.Count > 0 && c == stack.Pop()) {
                // do nothing
            } else {
                res = false;
                break;
            }
        }

        if (res && stack.Count > 0) {
            res = false;
        }

        return res;
    }
}
