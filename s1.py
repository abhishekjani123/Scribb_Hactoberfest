import math
 
def fact(t):
    for x in range(t):
        n = int(input())
        print(math.factorial(n))
 
 
if __name__ == '__main__':
    ans = int(input())
    fact(ans) 
