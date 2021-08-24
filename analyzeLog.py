filename = input('enter log file name to analyze : ')
logFile = open(filename,'r')

Lines = logFile.readlines()

count=int(input("how many lines, from start, to analyze (give 0 for full analysis)? : "))
i=0
prev=0
longestMiss=float("-inf")
totalMiss=0
sequence_stream=[]
toBreak=(count!=0)
missStart=0
missEnd=0
for line in Lines:

    #print(line)
    if(i==count and toBreak):
        break
    if i>0:
        words = line.split(' ')
        if words[0]=='From':
            sequence = words[2]
        else:
            sequence = words[4]
        pair = sequence.split('=')
        sNumber = int(pair[1])

        diff = sNumber-prev
        if diff>1:
            totalMiss=totalMiss+diff-1
            newLoss=diff-1
            if newLoss>longestMiss:
                missStart=prev
                missEnd=sNumber
            longestMiss=max(longestMiss,newLoss)
        prev=sNumber
        #sequence_stream.append(sNumber)

    i+=1
print('totoal icmp packet misses = ',totalMiss,' packets')
print('longest miss = ',longestMiss,' packets')
print('longest miss started with icmp packet number = ',missStart+1,' and ended with packet number = ',missEnd-1)


