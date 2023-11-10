#CO2412 Computational Thinking
#Analysing the factorial function ~ Week 3 lab sheet

#Exercise 2 – Programming Exercises lab 3
#1.	Write non recursive iterative (looping) solutions for:
#   Factorial where 0! = 1, N! = N(N – 1) if N > 0
#   maxnum (which returns the largest value from an unsorted array of integers.
#2.	Extend the maxnum function to return the highest and lowest values from an unsorted array of integers.

def factorial(n):

# single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial (n - 1)

# Driver Code
num = 5
print ("Factorial of ", num,"is",
factorial (num))
