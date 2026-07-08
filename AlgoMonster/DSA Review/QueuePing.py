from collections import deque

class QueuePing:

    def __init__(self) -> None:
        #Initialize the RecentCounter with an empty queue to store timestamps
        self.request_queue = deque()

    def ping(self, t: int) -> int:
        """
        Record a request at time t and return the number of request
        that have happened in the past 3000 milliseconds (including current request).

        Args:
            t: The timestamp of the current request in milliseconds.
            It's guaranteed that every call uses a larger t value than before

        Returns:
            The number of request in the time window [t-3000, t].
        """
        #Add the current timestamp to the queue
        self.request_queue.append(t)
        #Remove all timestamps that are outside the 3000ms window
        #Keep removing from the front while timestamp is older than t-3000
        while self.request_queue[0] < t-3000:
            self.request_queue.popleft()

        #Return the count of request within the valid time window
        return len(self.request_queue)

counter = QueuePing()
print(counter.ping(1))
print(counter.ping(100))
print(counter.ping(3001))
print(counter.ping(3002))
print(counter.ping(6002))
