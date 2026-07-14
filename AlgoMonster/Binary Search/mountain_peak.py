def peak_of_mountain_array(arr: list[int]) -> int:
    alen = len(arr)
    left = 0
    right = alen - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == alen - 1 or arr[mid] > arr[mid + 1]:      #Mountain peak will always be larger than next value
            boundary_index = mid
            right = mid - 1                                 #Check further left for elements
        else:                                               #If mid index is smaller than next then we move further right
            left = mid + 1

    return boundary_index

if __name__ == "__main__":
    #arr = [int(x) for x in input().split()]
    arr = [0,10,3,2,1,0]
    res = peak_of_mountain_array(arr)
    print(res)