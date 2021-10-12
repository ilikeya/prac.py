#a
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#b
for c in range(0,110,10):
    print(c, end=' ')
print()

#c
number_of_stars  =int(input("Number of Stars:"))
for i in range(number_of_stars):
    print('*',end='')
print()

#D
number_of_stars  =int(input("Number of Stars:"))
row = 1
while row <= number_of_stars:
    print("*" * row)
    row+=1
