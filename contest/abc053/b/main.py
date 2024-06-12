s = input()
l =s.index("A")

s_reversed = ''.join(list(reversed(s)))
r =s_reversed.index("Z")

print(len(s)-r-l)

