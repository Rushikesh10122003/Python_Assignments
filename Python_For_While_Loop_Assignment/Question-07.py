'''
factorial of given number
'''
num=int(input("Enter Number:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i   
print(f"Factorial of {num} is: {factorial}")