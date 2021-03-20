# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue

        self.queue.append(val)
        currentSum = sum(self.queue[-size:])

        print(currentSum / len(queue[-size:]))
        return currentSum / len(queue[-size:])


m = MovingAverage(3)
m.next(1)
m.next(10)
m.next(3)
m.next(5)