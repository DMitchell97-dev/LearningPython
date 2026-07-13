# def binary_search(arr: list[int], target: int) -> int:
#     if arr[len(arr)//2] > target:
#         return binary_search(arr[:len(arr)//2], target)
#     elif arr[len(arr)//2] < target:
#         return binary_search(arr[len(arr)//2:], target)
#     elif arr[len(arr)//2] == target:
#         return target
#     return -1

def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)