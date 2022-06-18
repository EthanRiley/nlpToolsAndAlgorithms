import numpy as np

class nlpUtil:
    
    @staticmethod
    def minEditDistanceNumpy(source, target):
        '''
        Minimum Edit Distance Aglorithm using a numpy array
        Does not work
        Want to fix, but got a version working using dictionaries
        '''
        lenSource = len(source)
        lenTarget = len(target)
        distanceTable = np.empty((lenTarget+1, lenSource+1))
        
        for i in range(lenSource):
            distanceTable[0, i] = int(i)
            
        for j in range(lenTarget):
            distanceTable[j, 0] = int(j)
            
        for i in range(1, lenSource+1):
            for j in range(1, lenTarget+1):
                if source[i-1] == target[j-1]:
                    distanceTable[j, i] = int(distanceTable[j-1, i-1])
                else:
                    distanceTable[j, i] = int(min(distanceTable[j-1, i], distanceTable[j, i-1], distanceTable[j-1, i-1])+1)
        
        return distanceTable[j, i]
    
    def minEditDistance(source, target):
        '''
        Minimum edit distance algorithm using 
        '''
        lenSource = len(source)
        lenTarget = len(target)
        
        distanceTable = {}
        for i in range(lenSource):
            distanceTable[i, 0] = i
            
        for j in range(lenTarget):
            distanceTable[0, j] = j
            
        for i in range(1, lenSource):
            for j in range(1, lenTarget):
                if source[i-1] == target[j-1]:
                    cost = 0
                else:
                    cost = 1
                distanceTable[i, j] = min(distanceTable[i, j-1]+1, distanceTable[i-1, j]+1, distanceTable[i-1, j-1]+cost)
                
        return distanceTable[i, j]
    