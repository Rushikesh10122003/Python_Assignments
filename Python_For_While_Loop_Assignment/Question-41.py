'''
print numbers which are perfect cubes between 1 and 100
'''

for i in range(1, 101):
    cube = i * i * i

    if cube <= 100:
        print(cube)
    else:
        break