class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            span = 1
            self.stack.append((price, span))

        else:
            tos = self.stack[-1]
            span = 1

            if price<tos[0]:
                self.stack.append((price, span))
                return span

            else:
                while price>=tos[0]:
                    days = self.stack.pop()
                    span += days[1]
                    tos = self.stack[-1]

            self.stack.append((price, span))

        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)