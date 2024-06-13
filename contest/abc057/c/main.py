n = int(input())
if n ==1:
    print(1)
    exit()

for i in range(1,n):
    if i**2 > n:
        break
    if n%i ==0:
        a = n//i
print(len(str(a)))

