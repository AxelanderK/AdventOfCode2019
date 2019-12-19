def chunks(lst, n):
    #"""Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

test = list(map(int, open('day2/input.txt','r').read().split(',')))
#copyx = test.copy()

for x in range(0, len(test), 4):
    if x < len(test) and test[x] != 99:

        var0 = test[x]
        var1 = test[x+1]
        var2 = test[x+2]
        var3 = test[x+3]

        #print(str(var0) + ' | ' + str(var1) + ' | ' + str(var2) + ' | ' + str(var3))
        if var0 == 1:
            test[var3] = test[var1] + test[var2]
        elif var0 == 2:
            test[var3] = test[var1] * test[var2]
        elif var0 == 99:
            break
    else:
        break
print(test)

# modules = list(map(int, open('day2/input.txt','r').read()))

# print(modules)