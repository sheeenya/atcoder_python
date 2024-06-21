# n = int(input())
# a = list(map(int,input().split()))

# #重複がどれかを検出 dup
# s = sorted(a)
# Dup = 0
# pre = -1
# for i in s:
#     if pre == i:
#         dup = pre
#     pre = i
# print("dup="+str(dup))
# #重複の位置を検出 left,right
# dupList = [i for i, x in enumerate(a) if x==dup]
# left = dupList[0]
# right = dupList[1]
# print("left="+str(left))
# print("right="+str(right))

# kCn

def kCn(k,n):
    ret = 1
    for k in range(min(n,k-n)):
        ret = ret * (n-k)
    return ret
print(kCn(5,2))


# #メイン処理
# for k in range(n+1):
#     if k == 0: #1個だけ選ぶ場合
#         print(n)
#     else: # 2個以上選ぶ場合





"""
1 2 3 4 5 6 7 4 8
4つとる場合、本来9C4
9*8*7*6/4/3/2 = 126
重複ケースは...
重複の外側の数字から(4-1)個を選ぶ数
つまり4C3 = 4
1234
1248
1348
2348


5x4/2x1
5x4x3/3x2x1

n

nCk - ?

重複を1個だけ使い、かつ
重複に挟まれているものを使わない場合に重複になる

まず重複がどれかを検出
重複がどこにあるかを探索


"""