class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        
        for word in strs:
            binary_arr = [0]*26
            for ch in word:
                i = ord(ch) - 97
                binary_arr[i] += 1
            key = tuple(binary_arr)
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)
        return list(hashMap.values())
        # print(hashMap)