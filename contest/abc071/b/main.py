S=input()
a="abcdefghijklmnopqrstuvwxyz"

for i in a:
    if not i in S:
        print(i)
        exit()

print("None")