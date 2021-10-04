
sequence = input().split()
number = input()
found = 0
print_string = ""
for i in range(len(sequence)):
    if sequence[i] == number:
        found = 1
        print_string += f"{i} "
if found is 0:
    print ("not found")
else:
    print(print_string)
