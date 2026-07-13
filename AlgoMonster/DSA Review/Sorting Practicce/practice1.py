def bubble_sort(nums: list[int]) -> list[int]:
    for i in nums:
        swapped = False
        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return nums
    return nums

def insertion_sort(unsorted_list: list[int]) -> list[int]:
    for i in range(1, len(unsorted_list)):
        current_item = unsorted_list[i]     #current item
        j = i - 1
        while j >= 0 and unsorted_list[j] > current_item:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1
        unsorted_list[j + 1] = current_item
    return unsorted_list

def selection_sort(unsorted_list: list[int]) -> list[int]:
    for i in range(0, len(unsorted_list)):
        min_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list


if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    #res = selection_sort(unsorted_list)
    #res = insertion_sort(unsorted_list)
    res = bubble_sort(unsorted_list)
    print(" ".join(map(str, res)))