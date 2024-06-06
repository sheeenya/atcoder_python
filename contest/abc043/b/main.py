S = input()
ans = []
for i in S:
    if i == "B":
        if ans !=[]:
            ans.pop()
    else:
        ans.append(i)
print("".join(ans))
