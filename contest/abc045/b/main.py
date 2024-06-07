sa = list(input())
sb = list(input())
sc = list(input())
st = "a"

for i in range(300):
    if st == "a":
        if not sa:
            print("A")
            exit()
        st=sa.pop(0)
        
    elif st == "b":
        if not sb:
            print("B")
            exit()
        st=sb.pop(0)
    else:
        if not sc:
            print("C")
            exit()
        st=sc.pop(0)
