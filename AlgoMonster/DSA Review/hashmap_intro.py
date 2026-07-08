def get_counter(arr: list[int]) -> dict[int, int]:
    #Initialize a hash map to store each number and its count
    counter: dict[int, int] = {}
    for num in arr:
        #Check if num is a key in the hash map
        if num in counter:
            #Update the count of num to increase by 1
            counter[num] += 1
        else:
            #set the count of num to 1
            counter[num] = 1
    return counter

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = get_counter(arr)
    for key in sorted(res.keys()):
        print(key, res[key])