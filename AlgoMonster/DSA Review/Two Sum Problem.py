def two_sum(arr: list[int], target: int) -> list[int]:
    #Dictionary to store number -> Index mapping
    d = {}

    #Iterate through the arry with index and value
    for index, n in enumerate(arr):
        remaining = target - n  #Calculate the remainder to find
        if remaining in d:      #Check to see if we've found the remainder before
            return [d[remaining], index]    #If yes return the pair

        d[n] = index    #If no add the number and index to the dictionary
    return []

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr, target)
    print(" ".join(map(str, res)))