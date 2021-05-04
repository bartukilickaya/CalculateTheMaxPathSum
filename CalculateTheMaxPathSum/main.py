### Check each number with is_prime ###
def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i <= n**(1./2): ### check till square root of n ###
            if n % i == 0:
                return False
            i += 1
        return True
def solve(lst):
    candidates = []
    candidates.append([0,lst[0][0]])
    for elem in lst[1:]: ### list traversal
        newlst = []
        i = 0
        while i < len(candidates): ### candidates of total list traversal
            if candidates[i][0] - 1 >= 0 and not is_prime(elem[candidates[i][0]-1]): ### check the left diagonal
                newlst.append([candidates[i][0]-1, elem[candidates[i][0]-1] + candidates[i][1]])
            if not is_prime(elem[candidates[i][0]]): ### check downward
                newlst.append([candidates[i][0], candidates[i][1] + elem[candidates[i][0]]])
            if candidates[i][0] + 1 <= len(elem) - 1 and not is_prime(elem[candidates[i][0] + 1]): ### check the right diagonal
                newlst.append([candidates[i][0] + 1, candidates[i][1] + elem[candidates[i][0] + 1]])
            i += 1
        candidates = []
        candidates = newlst
    max_total = 0
    for elem in candidates: ### find the lowest sum of all
        if max_total < elem[1]:
           max_total = elem[1]


    return max_total


def main():
    ####input from the user ###
    f = open("input.txt", "r")
    ### list with input lines ###
    lst = f.read().splitlines()
    lst = lst[:-1]
    tmplist = []
    i = 0
    ### get the list of list of intetegers ###
    for elem in lst:
        tmp = elem.split(" ")
        for elem2 in tmp:
            tmplist.append(int(elem2))
        lst[i] = tmplist
        tmplist = []
        i += 1

    res = solve(lst)
    print(res)

### Call main to compute
main()













