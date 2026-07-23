def remove_duplicates(arr: list[int]) -> int:
    left = 0
    for right in arr:
        if arr[left] != right:
            left += 1
            arr[left] = right
    return left + 1

if __name__ == "__main__":
    #arr = [int(x) for x in input().split()]
    arr = [0, 0, 1, 1, 1, 2, 2]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))