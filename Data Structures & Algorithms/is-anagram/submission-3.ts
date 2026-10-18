class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length)
            return false;

        const count: number[] = new Array(26).fill(0);
        const base = 'a'.charCodeAt(0)

        for (let i = 0; i < s.length; i++) {
            count[s.charCodeAt(i) - base]++;
            count[t.charCodeAt(i) - base]--;
        }

        return count.every(c => c == 0);
    }
}
