H,W = map(int,input().split())

if H%3==0 or W%3==0:
    print(0)
    exit()

ans =[]

for i in range(4):
    if i ==0: #縦に3分割
        a = round(H/3)*W
        b = round((H-round(H/3))/2)*W
        c = H*W-a-b
        ans.append(max(a,b,c)-min(a,b,c))

    if i ==1:
        b = round(W/2)*(H-round(H/3))
        c = H*W-a-b
        ans.append(max(a,b,c)-min(a,b,c))

    if i ==2:
        a = round(W/3)*H
        b = round((W-round(W/3))/2)*H
        c = H*W-a-b
        ans.append(max(a,b,c)-min(a,b,c))

    if i ==3:
        b = round(H/2)*(W-round(W/3))
        c = H*W-a-b
        ans.append(max(a,b,c)-min(a,b,c))
    
print(min(ans))

"""
縦に3分割、上と左右、横に3分割、左と上下の4パターンになる
4パターンについてそれぞれの最小値を算出し、最終的な答えを求める
"""