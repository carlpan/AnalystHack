import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from countvitae import getResumeCharCount

def getFrequencyList(count):
    '''
    Get list containing number of occurences.
    Returns corresponding frequency list.
    '''
    s = sum(count)
    return [(n/float(s))*100 for n in count]

def plotCount(countDict):
    '''
    Plot frequency as a function of alphabet character.
    '''
    # Sort input dictionary alphabetically
    charList = sorted(countDict)
    countList = [count for (char, count) in sorted(countDict.items())]
    frequencyList = getFrequencyList(countList)
    # Plotting
    labelPos = [2*(i+1) for i in range(len(charList))]
    plt.bar(labelPos, frequencyList, align='center')
    plt.xlim(0, len(charList))
    plt.xticks(labelPos, charList)
    plt.yticks(range(0, 12, 1), [str(x)+"%" for x in range(0, 12, 1)])
    plt.title('Resume Character Frequency')
    plt.savefig('output.png')
    plt.figure() 


if __name__== '__main__':
    plotCount(getResumeCharCount("resume.txt"))
    


