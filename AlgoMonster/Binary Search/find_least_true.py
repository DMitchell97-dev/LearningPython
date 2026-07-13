def find_boundary(arr: list[bool]) -> int:
    left, right, least_true_index = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            least_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return least_true_index


if __name__ == "__main__":
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)