# Pragrame to generate Fibonacci numbers

# Input

n = int(input("How many Fibonacci numbers you would like to generate : "))

# Process

i = 0
a = 0
b = 1

# output

while(i < n):
           if(i <= 1):
                      c = i
           else:
                      c = a + b
                      a = b
                      b = c
           print(c)
           i = i + 1
