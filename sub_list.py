from itertools import combinations

def sub_list(l):
    comb = []

    for i in range(len(l)+1):
        
        comb += [list[j] for j in combinations([1,2,3], i)]
    return comb


l1 = [1, 2, 3]

print("Intial list is: " + str(l1))

print("All sub list is : "+ str(sub_list(l1)))