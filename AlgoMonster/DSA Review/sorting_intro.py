
def self_sort_list(unsorted_list: list[int]) -> list[int]:
    sortedStack: list[int] = []
    tempStack: list[int] = []
    for item in unsorted_list:
        if sortedStack and item < sortedStack[-1]:
            while sortedStack and item < sortedStack[-1]:
                tempStack.append(sortedStack.pop())
            sortedStack.append(item)
            while tempStack:
                sortedStack.append(tempStack.pop())
        else:
            sortedStack.append(item)
    return list(sortedStack)

def sort_list(unsorted_list: list[int]) -> list[int]:
    for i in range(len(unsorted_list)):
        current = i
        #gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current], unsorted_list[current-1] = unsorted_list[current -1], unsorted_list[current]
            current -= 1
    return unsorted_list

def bubble_sort(unsorted_list: list[int]) -> list[int]:
    n = len(unsorted_list)

    #Iterate through all list elements in reversed order
    for i in reversed(range(n)):
        #Track whether a swap occured in this pass
        swapped = False
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
            if not swapped:
                return unsorted_list
    return unsorted_list
"""
Random job app question that I just decided to throw in here
"""
def string_map(text: str):
    character_count = {}
    output_string = ""
    for char in text.lower():
        if not character_count or char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    for index, char in enumerate(text):
        output_string += "".join([char, " (", str(index), ") - ", str(character_count[char.lower()]), " "])
    print(output_string)

if __name__ == "__main__":
    #unsorted_list = [int(x) for x in input().split()]
    string_map("HelloOo!!")
    #res = self_sort_list(unsorted_list)
    #res = sort_list(unsorted_list)
    #res = bubble_sort(unsorted_list)
    #print(" ".join(map(str, res)))