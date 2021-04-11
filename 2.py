Row = int(input("input Row:  "))
Column = int(input("input Column:  "))

for a in range(Row):
    if a%2 == 0:
        print('*', end='')
        for b in range(1,Column):
            if b%2 == 0:
                print('*', end='')
            else:
                print('#', end='')
    else:
        print('#', end='')
        for b in range(1,Column):
            if b%2 == 0:
                print('#', end='')
            else:
                print('*', end='')
    print()
