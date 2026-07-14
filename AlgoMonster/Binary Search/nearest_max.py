def first_not_smaller(arr: list[int], target: int) -> int:
    left, right, cur_max = 0, len(arr) -1, -1
    while left <= right:
        mid = (right + left) //2
        if target <= arr[mid]:
            right = mid - 1
            cur_max = arr[mid]
        elif target > arr[mid]:
            left = mid + 1
    return cur_max

def first_instance(arr: list[int], target: int) -> int:
    left, right, target_index = 0, len(arr) -1, -1
    while left <= right:
        mid = (right + left) //2
        if target <= arr[mid]:
            right = mid - 1
            if target == arr[mid]:
                target_index = mid
        elif target > arr[mid]:
            left = mid + 1
    return target_index

if __name__ == "__main__":
    print("Enter the array")
    arr = [int(x) for x in input().split()]
    #arr = [1,2,3,4,5,6,7,8,9,10]
    target = int(input())
    #target = 10
    res = first_not_smaller(arr, target)
    #res = first_instance(arr, target)
    print(res)
