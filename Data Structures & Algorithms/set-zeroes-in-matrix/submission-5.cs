public class Solution {
    public void SetZeroes(int[][] matrix) {
        var rows = new HashSet<int>();
        var cols = new HashSet<int>();

        for (var r = 0; r < matrix.Length; r++) {
            for (var c = 0; c < matrix[0].Length; c++) {
                if (matrix[r][c] == 0) {
                    rows.Add(r);
                    cols.Add(c);
                }
            }
        }

        for (var r = 0; r < matrix.Length; r++) {
            for (var c = 0; c < matrix[0].Length; c++) {
                if (rows.Contains(r) || cols.Contains(c)) {
                    matrix[r][c] = 0;
                }
            }
        }

    }
}
