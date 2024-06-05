#与えられる距離（メートル）
m = int(input())

if m < 100:
    print("00")
elif m < 5000:
    if m//100 < 10:
        print("0",m//100,sep="")
    else:
        print(m//100)
elif m < 30000:
    print(m//1000+50)
elif m < 70000:
    print((m//1000-30)//5+80)
else:
    print(89)