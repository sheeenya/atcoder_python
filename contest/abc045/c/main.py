S = input()
l = len(S)
bit_len = l-1
F = [] #作成する数式 ex. 123+4+5
ans = 0
for i in range((2**(l-1))):
    binary_string = f"{i:0{bit_len}b}"
    for j in range(l):
        F.append(list(S)[j])
        if j == l-1:
            F = ''.join(element for element in F if element)
            ans += eval(F)
            F = []
            break
        F.append(['+' if char == '1' else '' for char in list(binary_string)][j])
print(ans)
