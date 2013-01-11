'''
@author: tbulgerin
'''

arrCache = 1000000*[None]

def collatz(n):
    cycle = 1
    
    while(n != 1):
        # odd case
        if n & 1 == 1:
            n = 3 * n + 1  
        # even case
        else:
            n = n >> 1
            
        cycle += 1
        
    return cycle

def calcCycle(first, second):
    maxCycle = 0
    
    if first > second:
        first, second = second, first
    
    for i in range(first, second+1):
        # check to see if we have the value cached
        if arrCache[i] != None:
            cycle = arrCache[i]
        # otherwise calculate the cycle length
        # and cache the value
        else:
            cycle = collatz(i)
            arrCache[i] = cycle
            
        if(cycle > maxCycle):
            maxCycle = cycle
            
    return maxCycle
    

def main():

    while 1:
        try:
            # retrieve the input from the user
            values = raw_input()
            first, second = [int(i) for i in values.split(' ')]
        except:
            break
        
        #calculate the cycle length and display the result
        cycleLength = calcCycle(first, second)
        print first, second, cycleLength

if __name__ == '__main__':
    main()