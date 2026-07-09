def merge_sort_list(unsorted_list: list[int]) -> list[int]:
    n = len(unsorted_list)

    #Base case: A list of size 1 or 0 is already sorted
    if n<=1:
        return unsorted_list

    #Split the list into left and right halves
    midpoint = n//2
    left_list = merge_sort_list(unsorted_list[:midpoint])
    right_list = merge_sort_list(unsorted_list[midpoint:])

    result_list = []
    left_pointer, right_pointer = 0,0

    #Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            #If left list is empty, append element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            #If right list is empty, append element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            #Append smaller element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:   #Append smaller element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    return result_list

def sort_list_interval(unsorted_list: list[int], start: int, end: int) -> None:
    #If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    #Using last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    #Partitioning process
    while start_ptr < end_ptr:
        #Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        #Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        #Swap if pointers havent met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
    #Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end-1] = unsorted_list[end-1], unsorted_list[start_ptr]

    #Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def quick_sort(unsorted_list: list[int]) -> list[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = merge_sort_list(unsorted_list)
    res2 = quick_sort(unsorted_list)
    print(" ".join(map(str, res)))
    print(" ".join(map(str, res2)))
