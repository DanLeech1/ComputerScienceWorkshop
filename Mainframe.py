
#Week 3 Lab
amillion = 5
x = 0
list1 = []

for i in range(amillion):
    list1.append(x)
    x = x + 1
    print(list1)

y = 1
list2 = []
for i in range(10):
    list2.append(y)
    print(list2)
    y = y + 2

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
p = 0
for i in range(len(alphabet)):
    print(alphabet[p])
    p = p + 1