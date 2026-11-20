'''
Multiplication table of given number
'''

num=int(input("Enter Number:"))
Table=[]
for i in range(1, 11):
    table=num*i
    Table.append(table)
print(f"Multiplication table of {num} is: {Table}")
