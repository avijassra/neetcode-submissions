class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        output = []
        seen = {}

        for i, s in enumerate(strs):
            # print(s)
            sorted_s = "".join(sorted(s))
            # print(sorted_s)
            if sorted_s in seen:
                output[seen[sorted_s]].append(s)
            else:
                seen[sorted_s] = len(output)
                output.append([s])

        return output