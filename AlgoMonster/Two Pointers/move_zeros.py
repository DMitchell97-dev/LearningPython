def move_zeros(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):   #Walk through the array as fast
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1               #Increment at slow
    pass

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    #nums = [3,1,0,1,3,8,9]
    move_zeros(nums)
    print(" ".join(map(str, nums)))