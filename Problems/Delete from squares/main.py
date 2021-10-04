key_val = int(input())

popped = squares.pop(key_val, "There is no such key")

if key_val in squares:
    print(squares)
else:
    print(popped)
    print(squares)
