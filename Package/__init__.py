#Nicholas Delli Carpini

from time import perf_counter

# Tests the input value to make sure its is a int greater than 0
def testNumber():
    for i in range (0, 3):
        x = input()
        try:
            x = int(x)
        except ValueError: 
            print("Error: Invalid Value - Please Enter Any Integer Greater than 0")
            x = 0
            continue
        if (x <= 0):
            print("Error: Invalid Value - Please Enter Any Integer Greater than 0")
            x = 0
            continue
        break
    if (x == 0):
        print("\nMaximum Attempts Used - Please Restart the Program to Try Again")
    else:
        return x
    
# Prints the time in a more readable format using shorthand units and only 2 decimal places
def printTime(ans):
    if (ans > 1e-02):
        print ("Time: %.2f" % ans, "s")
    if (ans <= 0.01 and ans > 0.00001):
        ans = ans * 1000
        print ("Time: %.2f" % ans, "ms")
    if (ans <= 0.00001 and ans > 0.00000001):
        ans = ans * 1000000
        print ("Time: %.2f" % ans, "\u00B5s")
    if (ans <= 0.00000001):
        ans = ans * 1000000000
        print ("Time: %.2f" % ans, "ns")

# Euclid method, copied straight off the instruction sheet   
def euclid(n,m):
    while n != 0:
        x = m % n
        m = n
        n = x
    return m

# Consecutive Integer Checking Algorithm, a little messy but overall should be fairly efficient
def cica(n, m):
    if (n <= m):
        x = n
    else:
        x = m
    while True:
        if (m % x == 0):
            if (n % x == 0):
                break
            else:
                x = x - 1
                continue
        else:
            x = x - 1
            continue
    return x

# Helper function for Middle School Procedure, gets all the prime numbers and numerically orders them into an array
def primeFactors(x):
    factors = []
    y = 2
    while (x > 1):
        while (x % y == 0):
            factors.append(y)
            x /= y
        y += 1
    return factors

# Middle School Procedure, messy and could probably be more efficient, but I couldn't figure out a way to make it more
# efficient without compromising correctness
def msp(n, m):
    total = 1
    fn = primeFactors(n)
    fm = primeFactors(m)
    for i in range(0, len(fn)):
        for j in range(0, len(fm)):
            if (fn[i] == fm[j]):
                total = total * fm[j]
                fn[i] = None
                fm[j] = None
    return total

# Prints the final results
def printResults(n,m):
    print("\nValues:", m, ",", n)
    print("\nUsing Euclid's Algorithm")
    print("GCD:", euclid(n, m))
    start = perf_counter()      # ]
    euclid(n, m)                # ] Calculates the time seperately from printing the answer in order to give the most
    end = perf_counter()        # ] accurate time. Gets the uptime of the system before and after the function call and
    time = end - start          # ] then subtracts them, the uses printTime to make the numbers easier on the eyes
    printTime(time)             # ]
    
    print("\nUsing Consecutive Integer Checking")
    print("GCD:", cica(n, m))
    start = perf_counter()
    cica(n, m)
    end = perf_counter()
    time = end - start
    printTime(time)
    
    print("\nUsing the 'Middle School Procedure'")
    print("GCD:", msp(n, m))
    start = perf_counter()
    msp(n, m)
    end = perf_counter()
    time = end - start
    printTime(time)

print("Welcome to the GCD Algorithm Comparison Tool")

print("\nPlease Input a Value for the First Number (M)")
m = testNumber()

print("\nPlease Input a Value for the Second Number (N)")
n = testNumber()

print("\nPlease Wait...")
printResults(n,m)

print("\nPress Enter to Quit")
input()
    