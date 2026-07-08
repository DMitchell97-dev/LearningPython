import queue
from collections import deque

def rotate_left_till_zero(nums: list[int]) -> list[int]:
    #Initialize a new deque out of nums
    queue = deque(nums)
    #continue the loop till front of queue is 0
    while queue[0] != 0:
        # remove the front of the queue and add it to the end
        queue.append(queue.popleft())
    #Create a list out of the queue
    return list(queue)

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = rotate_left_till_zero(nums)
    print(" ".join(map(str, res)))