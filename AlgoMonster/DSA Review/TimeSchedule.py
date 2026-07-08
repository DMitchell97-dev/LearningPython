#Input: arr[] = [[1, 3], [2, 4], [6, 8], [9, 10]]
# Output: [[1, 4], [6, 8], [9, 10]]
# Explanation: In the given intervals, we have only two overlapping intervals [1, 3] and [2, 4]. Therefore, we will merge these two and return [[1, 4]], [6, 8], [9, 10]].
#
# Input: arr[] = [[7, 8], [1, 5], [2, 4], [4, 6]]
# Output: [[1, 6], [7, 8]]
# Explanation: We will merge the overlapping intervals [[1, 5], [2, 4], [4, 6]] into a single interval [1, 6].

testData = [[1,3], [2,4], [6,8], [9,10]]

def mergeOverlap(arr):

    arr.sort()
    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res

if __name__ == '__main__':
    #arr = [[1,3], [2,4], [6,8], [9,10]]
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])