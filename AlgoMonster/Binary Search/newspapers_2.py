def newspapers_split(newspapers_read_times: list[int], num_coworkers: int) -> int:
    left = max(newspapers_read_times)
    right = sum(newspapers_read_times)
    min_read_time = right

    while left <= right:
        mid = (left + right) // 2

        if verify_read_time(newspapers_read_times, num_coworkers, mid):
            right = mid - 1
            min_read_time = mid
        else:
            left = mid + 1

    return min_read_time

def verify_read_time(arr: list[int], workers: int, target: int) -> bool:
    readers, time_read = 1, 0
    for hour in arr:
        if time_read + hour > target:
            readers += 1
            time_read = hour
        else:
            time_read += hour
    if readers <= workers:
        return True
    else:
        return False

if __name__ == "__main__":
    # newspapers_read_times = [int(x) for x in input().split()]
    # num_coworkers = int(input())
    # Test Case 1
    # newspapers_read_times = [7, 2, 5, 10, 8]
    # num_coworkers = 2

    # Test Case 2
    newspapers_read_times = [12, 8, 15, 20, 6, 9, 14, 3, 18, 7, 11, 5, 22]
    num_coworkers = 4

    # Test Case 3
    # newspapers_read_times = [5, 10, 3, 8, 12, 7, 6, 4, 9, 11]
    # num_coworkers = 3
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)