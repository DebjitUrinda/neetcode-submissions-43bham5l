class Solution:
    def calPoints(self, operations: List[str]) -> int:
        import re
        record = [0]
        ret_sum = 0

        for op in operations:
            if re.fullmatch(r"[0-9]+", op):
                record.append(op)
            elif re.fullmatch(r"\+", op):
                record.append(int(record[-1]) + int(record[-2]))
            elif op == "C":
                record.pop()
            elif op == "D":
                push = 2*int(record[-1])
                record.append(push)

        for i in record:
            print(i)
            ret_sum += int(i)

        return ret_sum