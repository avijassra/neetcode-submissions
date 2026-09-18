class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        encode_str = ">[?@?]<".join(strs)

        print(encode_str)

        return f'<{encode_str}>'

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        list_s = s[1:len(s)-1].split(">[?@?]<")
        print(list_s)

        return list_s