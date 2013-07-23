# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end of the string to hold
# the additional characters, and that you are given the 'true' length of the string.
# (Note: if implementing in java/python, please use a character array so that you can 
# perform this operation in place

def replaceSpaces(inputstring,length):
    spacecount=0
    for i in xrange(length):
        if inputstring[i] == ' ':
            spacecount += 1

    newlength = length + spacecount*2

    for i in xrange(length-1,-1,-1):
        if inputstring[i] == ' ':
            inputstring[newlength-1] = '0'
            inputstring[newlength-2] = '2'
            inputstring[newlength-3] = '%'
            newlength -= 3
        else:
            inputstring[newlength-1] = inputstring[i]
            newlength -= 1

    return inputstring

###
# testing
###

inputstring = list('Mr John Smith    ')
inputlength = 13
expectedoutputstring = list('Mr%20John%20Smith')

outstring = ''.join(replaceSpaces(inputstring,inputlength))

expectedoutstring = ''.join(expectedoutputstring)

if outstring == expectedoutstring:
    print "Passed Test 1"


#edge case where string is all spaces, 2 that need to be replaced, and 4 for the expansion room, 6 spaces total
inputstring = [" "," "," "," "," "," "]
inputlength = 2
expectedoutputstring = ["%","2","0","%","2","0"]

outstring = ''.join(replaceSpaces(inputstring,inputlength))

expectedoutstring = ''.join(expectedoutputstring)

if outstring == expectedoutstring:
    print "Passed Test 2"
