j = [1,2,2,3,4,4,5,1]

def list_count(l):
    output = []
    seen = set()
    for n in l:
        if n not in seen:
            seen.add(n)     #Add the new number to our set
            n_count = l.count(n)    #l.count() I guess just does the work of counting how many times that number is in said list
            output.append((n, n_count))

    return output

print(list_count(j))