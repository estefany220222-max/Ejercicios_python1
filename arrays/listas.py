'''
Colecciones en Python
Listas (list)
'''

my_list = [3, 1, 5, 7, 8, 1, 5, 2]

print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[3])
print(my_list[-1])
print()

print(len (my_list))
print()

my_other_list = ['hi', True, 1, 1.3, [10, 11]]
print(my_other_list[4][0])
print()

for i in range (len (my_other_list)):
    print(i, ' -> ', my_other_list[i])
print()

for i in my_other_list:
    print(i)
print()

numbers = [3,2,4,5,1,8,7,9]
for i in numbers:
    print(i)
numbers.append(15) #inserta algo al final
numbers.append(35)
print(numbers)
numbers.pop() #extrae el ultimo valor
print(numbers)
numbers.reverse() #invierte los elementos
print(numbers)
numbers.sort() #ordena los elementos
print(numbers)
numbers.clear()
print(numbers)