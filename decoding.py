string = input("Please enter data bytes as hexadecimal: ")
lst = string.split(" ")

print(chr(254))

lst_int = []
for element in lst:
    lst_int.append(int(element, 16))

for element in lst_int:
    print(element, end=' ')

for element in lst_int:
    print(chr(element))
