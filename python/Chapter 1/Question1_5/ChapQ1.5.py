# Implement a method to perform basic string compression using the counts of 
# repeated characters. For example, the string aabccccaaa would become
# a2b1c4a3. If the 'compressed' string would not become smaller than the original
# string, your method should return the original string.

def countCompression(instring):
    """ Check if compression would create a longer string """
    if (instring == None or len(instring) == 0):
        return 0
    last = instring[0]
    size = 0
    count = 1
    for char in instring[1:]:
        if char == last:
            count += 1
        else: 
            last = char
            size += 1 + len(str(count))
            count = 1
    size += 1 + len(str(count))
    return size

def compressBad(instring):
    size = countCompression(instring)
    if size >= len(instring):
        return instring

    mystr = ''
    last = instring[0]
    count = 1
    for char in instring[1:]:
        if char == last:
            count += 1
        else:
            mystr += last + str(count)
            last = char
            count = 1
    return mystr + last + str(count)



def compressBetter(instring):
    size = countCompression(instring)
    if size >= len(instring):
        return instring
    
    mystr = []
    last = instring[0]
    count = 1
    for char in instring[1:]:
        if char == last:
            count += 1
        else:
            mystr.append(char)
            mystr.append(str(count))
            count = 1
            last = char            
    #final write
    mystr.append(last)
    mystr.append(str(charcount))
    
    return ''.join(mystr)

#testing

tocompress = "aabcccccaaa"

if compressBad(tocompress) == "a2b1c5a3":
    print "Test 1 Passed"
else:
    print "Test 1 Failed"

tocompress2 = "aabca"
if compressBetter(tocompress2) == tocompress2:
    print "Test 2 Passed"
else:
    print "Test 2 Failed"

