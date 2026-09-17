class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let res = true;
        let closingTags = [];

        for(let str of s) {
            if(str === '(') {
                closingTags.push(')');
            } else if(str === '{') {
                closingTags.push('}');
            } else if(str === '[') {
                closingTags.push(']');
            } else if(closingTags.length > 0 && str === closingTags[closingTags.length-1]) {
                closingTags.pop();
            } else {
                res = false;
                break;
            }
        }

        if (res && closingTags.length > 0) {
            res = false;
        }
        
        return res;
    }
}
