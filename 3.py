Row = int(input("input Row:  "))
Column = int(input("input Column: "))

for a in range(1,Row+1):
    for b in range(1,Column+1):
        print(str(a*b)+' ', end='')
    print()
  
