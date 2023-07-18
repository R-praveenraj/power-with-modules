# Power with Modules
# You are given A, B and C .
# Calculate the value of (A ^ B) % C

# Input 1:
# A = 2 B = 3 C = 3
# Input 2:
# A = 5 B = 2 C = 4
# Output 1: 2
# Output 2: 1
def powerModules(a,b,c):
    a=a%c
    result=1
    while(b>0):
        result=(result*a)
        result=result%c
        b-=1
    return result

a=int(input())
b=int(input())
c=int(input())
print(powerModules(a,b,c))