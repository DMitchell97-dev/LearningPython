def merge_list(test_input_list1: list[int], test_input_list2: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    while i < len(test_input_list1) or j < len(test_input_list2):
        if i == len(test_input_list1):
            result.append(test_input_list2[j])
            j += 1
        elif j == len(test_input_list2):
            result.append(test_input_list1[i])
            i += 1
        elif test_input_list1[i] <= test_input_list2[j]:
            result.append(test_input_list1[i])
            i += 1
        else:
            result.append(test_input_list2[j])
            j += 1
    return result

if __name__ == "__main__":
    list1 = []
    list2 = [2,4,6]
    print(merge_list(list2, list1))