class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let res = true;
        let openTags = {
            '(': ')',
            '{': '}',
            '[': ']'
        };
        let stack = [];

        for(let str of s) {
            if(openTags[str]) {
                stack.push(openTags[str]);
            } else if(stack.length > 0 && str === stack[stack.length-1]) {
                stack.pop();
            } else {
                res = false;
                break;
            }
        }

        if (res && stack.length > 0) {
            res = false;
        }
        
        return res;
    }
}
