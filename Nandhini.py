# Python3 Program to compute the largest prime number that is a sum of most consecutive primes

primeNumbs = []
sumList = []
b = []
most = []

# from math lib import sqrt method
from math import sqrt
 
# Function to compute the prime number
def checkPrime(numberToCheck) :
    if numberToCheck == 1 :
        return False
    
    for i in range(2, int(sqrt(numberToCheck)) + 1) :
        if numberToCheck % i == 0 :
            return False
    return True

# Function to compute the largest prime number that is a sum of most consecutive primes
def findSum(primeNumbs):
    b.clear()
    summ = 0
    
    for i in range(len(primeNumbs)):
        b.clear()
        summ = 0
        count = 0
        j = i
        
        while j < (len(primeNumbs)):
            summ += primeNumbs[j]
            count += 1
            b.append(primeNumbs[j])
            if summ < r and checkPrime(summ):
                if count > 1: 
                    most.append(len(b))
                    sumList.append(summ)
            j += 1
    try:
        mostNumbs = most[0]
        for k in most:
            if k > mostNumbs:
                mostNumbs = k
        index = most.index(mostNumbs)
        print("\t\t>> The largest prime number that is a sum of most consecutive primes is",sumList[index])
    except IndexError as e:
        print("\n\t\t>> There is no prime number that is a sum of most consecutive primes below.")

# Function to iterate the loop from l to r to check if the currentnumber is prime and store it in primeNumbs list
def primeSum(l, r) :
    for i in range(l, r) :
        # Check for prime
        isPrime = checkPrime(i)
        if (isPrime) :
            primeNumbs.append(i)

    finalSum = findSum(primeNumbs)
    return finalSum
            
            
if __name__ == "__main__" :
    print("\tWELCOME TO THE PROGRAM TO COMPUTE THE LARGEST PRIME NUMBER THAT IS THE SUM OF MOST CONSECUTIVE PRIMES\n")
    number = int(input ("\t\t>> Please enter the number : "))
    l, r = 2, number
 
    # Call the function with l and r
    primeSum(l, number)
    print("\n\t\t\t\t\t\tTHANK YOU")
    
