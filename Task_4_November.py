'''
'''The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….. 
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.
'''

#the Fibonacci series=  where the next number is found out by adding the previous two numbers

n_terms = int(input("How many terms the user wants to print? "))

n_1 = 0
n_2 = 1
count = 0

print("The fibonacci sequence of the numbers is:")
while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1
