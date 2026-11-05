class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def formString(s, b, e):
            print(s)

            if b == 0 and e == 0:
                print(s)
                res.append(s)
                return

            if e > b and e > 0: formString(s + ')', b, e-1)
            if b > 0: formString(s + '(', b-1, e)

        formString('', n, n)
        return res