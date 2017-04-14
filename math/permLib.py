#permutation generator
#recursive algorithm generates all permutations of set
def permutationHelper(permutation, permutations, set):
    if len(set) > 0:
        for i in range(0, len(set)):
            #choose the next element from the set
            element = set[0]
            permutation.append(element)
            set.remove(element)
		
            #if this is the only element left, this is a permutation
            if len(set) == 0:
                temp = [x for x in permutation]
                permutations.append(temp)
            else: #make all possible choices with remaining elements
                permutationHelper(permutation, permutations, set)
		
	    #undo this choice and put element at the end of the set	
            set.append(element)
            permutation.remove(element)
            
def generatePermutations(set):
    permutations = []
    permutation = []
    permutationHelper(permutation, permutations, set)
    return permutations

print generatePermutations(['a','b','c'])

