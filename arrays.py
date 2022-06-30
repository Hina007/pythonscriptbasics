#importing array
import array as arr

#declaring array with int type
a = arr.array ('i', [1, 2, 3])

print (a[0])
print(end="")

for i in range(0, len(a)):
    print (a[i])

a.insert(0, 5)
for i in range(0, len(a)):
    print (a[i])

a.append(6)
for i in range(0, len(a)):
    print (a[i])

a.pop(2)
for i in range(0, len(a)):
    print (a[i])



