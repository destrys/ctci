from collections import defaultdict

#Given two strings, write a method to decide if one is a permutation of the other.

# O(n^2)
def isPermutation(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        for char in s1:
            if s2.find(char)==-1:
                return False
            else:
                s2.replace(char,"",1)
        return True

# big O complexity depends on python list sort complexity, which should be better than O(n^2)
def isPermutationSort(s1,s2):
    if len(s1) != len(s2):
        return False

    #sort both strings, check if they are equal
    if sorted(s1) == sorted(s2):
            return True
    return False

#O(n)
def isPermutationHash(s1,s2):
    #using a dict as a hash table to count occurences, then comparing the 2 dict
    charcountdict1 = makeCharCountDict(s1)
    for char in s2:
        charcountdict1[char] -= 1
        if charcountdict1[char] < 0:
            return False        
    return True

#make a dict out of a string, tallying the use of each unique character
def makeCharCountDict(instring):
    returndict = defaultdict(int)
    for char in instring:
        returndict[char] += 1
    return returndict

    
#testing

#permutation
postest1 = ["abcdefgh","abcdefhg"]

#not permutation
negtest2 = ["abcdefgh","gfsdgsdffsd"]

#not permutation
negtest3 = ["abcdefgh","gfsdgsdf"]


#list of all functions to test
funclist = [isPermutation,isPermutationSort,isPermutationHash]

for func in funclist:
    print "Testing function " + str(func)    
    if func(postest1[0],postest1[1]):
        print "Test 1 passed"
    if not func(negtest2[0],negtest2[1]):
        print "Test 2 passed"
    if not func(negtest3[0],negtest3[1]):
        print "Test 3 passed"
                


