# Problem: https://leetcode.com/problems/print-in-order
# Runtime: 3497 ms

class Foo:
    def __init__(self):
        self.idx = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while (self.idx != 0):
            pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.idx = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while (self.idx != 1):
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.idx = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while (self.idx != 2):
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()