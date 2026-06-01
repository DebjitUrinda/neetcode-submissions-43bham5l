class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for ch in s:
            if ch in hashMap:  # opening bracket
                stack.append(ch)
            else:              # closing bracket
                if not stack:
                    return False

                if hashMap[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0