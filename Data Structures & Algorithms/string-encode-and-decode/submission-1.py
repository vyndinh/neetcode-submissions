class Solution:

    def encode(self, strs: List[str]) -> str:
        merstr = ""
        for s in strs:
            merstr += f"{len(s)}#{s}"
        return merstr

    def decode(self, s: str) -> List[str]:
        
        # split_str = s.split()
        # for s in split_str:
        #     arr.append(s)
        # if len(arr) == 0:
        #     return [""]
        # return arr

        arr = []
        i = 0
        while i < len(s):
            delim_index = s.find('#', i)
            length = int(s[i:delim_index])
            start = delim_index + 1
            end = start + length
            arr.append(s[start:end])

            i = end
        return arr


