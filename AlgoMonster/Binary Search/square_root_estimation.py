def square_root(n: int) -> int:
    max, min = n, 1
    nearest_root = 0
    if n * n == n:
        return n
    while min <= max:
        mid = (max + min) // 2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            max = mid - 1
        else:
            min = mid + 1
            nearest_root = mid
    return nearest_root

if __name__ == "__main__":
    n = int(input())
    #n=1
    res = square_root(n)
    print(res)