'''
demonstrate all list methods
'''

items = [30, 10, 20, 10]

print("Original:", items)

items.append(40)
print("append:", items)

items.extend([50, 60])
print("extend:", items)

items.insert(1, 15)
print("insert:", items)

items.remove(10)
print("remove:", items)

print("pop removed:", items.pop())

print("copy:", items.copy())

print("count:", items.count(10))

print("index:", items.index(20))

items.sort()
print("sort:", items)

items.reverse()
print("reverse:", items)

items.clear()
print("clear:", items)