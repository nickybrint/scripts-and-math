#permutation generator
#recursive algorithm generates all permutations of set
def permHelper(perm, perms, set):
    if len(set) > 0:
        for i in range(0, len(set)):
            num = set[0]
            perm.append(num)
            set.remove(num)
            if len(set) == 0:
                temp = [x for x in perm]
                perms.append(temp)
            permHelper(perm, perms, set)
            set.append(num)
            perm.remove(num)
            
def generatePerms(set):
    perms = []
    perm = []
    permHelper(perm, perms, set)
    return perms


def generateCombinations(set, length, minLength):
        combs = []
        if len(set) <= length and len(set) >= minLength:
            combs.append(list(set))
        if len(set) == 1:
            return combs
        for n in range(0, len(set)):
                setCopy = [x for x in set]
                setCopy.remove(set[n])
                #setCopy.remove(set[n])
                if len(setCopy) <= length and len(setCopy) >= minLength:
                        combs.append(setCopy)
                combHelper(setCopy, length, combs, minLength)
        uniqueCombs = []
        for comb in combs:
                if not comb in uniqueCombs:
                        uniqueCombs.append(comb)
        return uniqueCombs


def combHelper(set, length, combs, minLength):
        if len(set) > minLength:
                for n in range(0, len(set)):
                        setCopy = [x for x in set]
                        setCopy.remove(set[n])
                        if len(setCopy) <= length and len(setCopy) >= minLength:
                                combs.append(setCopy)
                        combHelper(setCopy, length, combs, minLength)

                        
                

#print generatePerms(['a','b','c','d'])
#print generateCombinations(range(0,4), 4, 4)
