N=int(input())
S1=list(input())
S2=list(input())
ans=1

if S1.pop()==S2.pop(): #縦
    ans *= 3
    now = "tate"
else: #横
    S1.pop()
    S2.pop()
    ans *= 6
    now = "yoko"

while len(S1)>0:
    if S1.pop()==S2.pop(): #縦
        if now == "tate":
            ans = (ans*2)%1000000007
        else:
            ans = (ans*1)%1000000007
        now = "tate"
    else: #横
        if now == "tate": 
            ans = (ans*2)%1000000007
        else:
            ans = (ans*3)%1000000007
        S1.pop()
        S2.pop()
        now = "yoko"

print(ans)


    
    


"""
縦置きか横置きかで場合の数が変わる
一番左について、縦なら3通り、横なら6通り
縦から縦、縦から横は2通り
横から縦は1通り、横から横は3通り
S1とS2が同じであれば縦、違うなら横と判定、横ならもう一つ消す
"""