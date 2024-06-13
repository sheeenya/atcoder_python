N = int(input())
s = input()
t = [""]*N
trans_s = (s.replace("o","1 ")).replace("x","-1 ")
trans_s = list(trans_s.split(" "))

for i in range(4):
    if i ==0:
        t[0] = 1
        t[N-1] = 1

        for j in range(N-2):
            t[j+1] = t[j-1]*t[j]*int(trans_s[j])
        if t[N-1] == t[N-3]*t[N-2]*int(trans_s[N-2]) and t[0] == t[N-2]*t[N-1]*int(trans_s[N-1]) :
            for i in range(len(t)):
                if t[i] == 1:
                    a =str(t[i]).replace("1","S")
                else:
                    a =str(t[i]).replace("-1","W")
                t[i]= a
            print("".join(t))
            exit()

    elif i ==1:
        t[0] = 1
        t[N-1] = -1

        for j in range(N-2):
            t[j+1] = t[j-1]*t[j]*int(trans_s[j])
        if t[N-1] == t[N-3]*t[N-2]*int(trans_s[N-2]) and t[0] == t[N-2]*t[N-1]*int(trans_s[N-1]) :
            for i in range(len(t)):
                if t[i] == 1:
                    a =str(t[i]).replace("1","S")
                else:
                    a =str(t[i]).replace("-1","W")
                t[i]= a
            print("".join(t))
            exit()

    elif i ==2:
        t[0] = -1
        t[N-1] = 1

        for j in range(N-2):
            t[j+1] = t[j-1]*t[j]*int(trans_s[j])
        if t[N-1] == t[N-3]*t[N-2]*int(trans_s[N-2]) and t[0] == t[N-2]*t[N-1]*int(trans_s[N-1]) :
            for i in range(len(t)):
                if t[i] == 1:
                    a =str(t[i]).replace("1","S")
                else:
                    a =str(t[i]).replace("-1","W")
                t[i]= a
            print("".join(t))
            exit()


    elif i ==3:
        t[0] = -1
        t[N-1] = -1

        for j in range(N-2):
            t[j+1] = t[j-1]*t[j]*int(trans_s[j])
        if t[N-1] == t[N-3]*t[N-2]*int(trans_s[N-2]) and t[0] == t[N-2]*t[N-1]*int(trans_s[N-1]) :
            for i in range(len(t)):
                if t[i] == 1:
                    a =str(t[i]).replace("1","S")
                else:
                    a =str(t[i]).replace("-1","W")
                t[i]= a
            print("".join(t))
            exit()

print(-1)