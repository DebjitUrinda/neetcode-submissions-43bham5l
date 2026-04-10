class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = len(s)
            encoded = encoded + str(l) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        while i < len(s):
            # find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            strs.append(s[start:end])
            i = end  # move to the start of the next encoded part
        return strs