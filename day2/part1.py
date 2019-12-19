def chunks(lst, n):
    #"""Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

test = list(map(int, open('day2/test.txt','r').read().split(',')))

for x in range(0, len(test), 4):
    var0 = test[x]
    var1 = test[x+1]
    var2 = test[x+2]
    var3 = test[x+3]

    print(str(var0) + ' | ' + str(var1) + ' | ' + str(var2) + ' | ' + str(var3))

    if var0 == 1:
        print('1')
    elif var0 == 99:
        break;
print(test)

# modules = list(map(int, open('day2/input.txt','r').read()))

# print(modules)