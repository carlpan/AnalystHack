import re
import collections

def refactorResume(inputfilename, outputfile):
    '''
    Strip all non-alphabetic, numeric, and whitespace characters.
    Write the result to a new file.
    '''
    with open(inputfilename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.lower()
            # Ignore digits, underscores and 
            # characters other than alphabetic
            l = re.findall(r"[^\W\d_]+", line)
            outputfile.write("".join(l))

def getResumeCharCount(inputfilename):
    '''
    Strip all non-alphabetic, numeric, and whitespace characters.
    Return a dictionary with
        - key: alphabet character
        - value: number of occurences
    '''
    charCount = collections.defaultdict(int)
    with open(inputfilename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.lower()
            l = re.findall(r"[^\W\d_]+", line)
            for c in "".join(l):
                charCount[c] += 1
    return dict(charCount)

def test():
    '''
    Test cases
    '''
    # Case 1
    testDict1 = {'a':1, 'b':1, 'c':1, 'd':1, 'e':1}
    testString1 = "ab_1414cd-e%"
    inputfile1 = open('testoutput1', 'w')
    inputfile1.write(testString1)
    inputfile1.close()
    result1 = getResumeCharCount('testoutput1')
    if cmp(result1, testDict1) == 0:
        print 'Pass test 1'

    # Case 2
    testDict2 = {'a':2, 'f':1, 'l':2, 'm':1, 'y':1}
    testString2 = "Fall 2009 - May 2013"
    inputfile2 = open('testoutput2', 'w')
    inputfile2.write(testString2)
    inputfile2.close()
    result2 = getResumeCharCount('testoutput2')
    if cmp(result2, testDict2) == 0:
        print 'Pass test 2'
        
    # Case 3
    testDict3 = {'k':2, 'a':2, 'r':1, 'l':2, 'p':1, 'n':1, 'o':4, 'u':1, 't':1, 'c':1, 'm':1}
    testString3 = ", 60615 (734)-358-6152 karlpan66@outlook.com"
    inputfile3 = open('testoutput3', 'w')
    inputfile3.write(testString3)
    inputfile3.close()
    result3 = getResumeCharCount('testoutput3')
    if cmp(result3, testDict3) == 0:
        print 'Pass test 3'
    

if __name__=="__main__":    
    test()



    
