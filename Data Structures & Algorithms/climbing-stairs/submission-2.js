class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let step = [];
        step[1] = 1;
        step[2] = 2;

        for(let i = 3; i <= n; i++) {
            step[i] = step[i-1] + step[i-2];
        }

        return step[n];
    }
}
