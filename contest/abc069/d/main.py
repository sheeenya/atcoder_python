H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))
snake=[]

for i in range(N):
    for j in range(a[i]):
        snake.append(str(i+1))

for s in range(H):
    if s%2==0:
        print(" ".join(snake[s*W:s*W+W]))
    else:
        print(" ".join((snake[s*W:s*W+W])[::-1]))

"""
ヘビみたいに塗っていけばいいだけ
マスの数だけloopさせて、指定するマスを
グネグネさせればOK
"""