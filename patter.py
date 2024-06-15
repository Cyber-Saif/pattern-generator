lines = int(input('how many star do you want: '))
pattern = input('type symbole you want: ')


#this for loop is going to create rows
for i in range(lines):
    # this for loop wil going to create colums for pattern
    for j in range(i + 1):
        print(pattern, end= " ")
    print()    

