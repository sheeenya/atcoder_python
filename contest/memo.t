#int型での複数入力
a,b,c = map(int,input().split())

#スペース区切りの入力をリストに
a = list(map(int,input().split()))

#数字を5桁の2進数に
n = int
format(n,"05b")

#可変の桁数に
i = int #元の数字
bit_len = int #桁数
binary_string = f"{i:0{bit_len}b}"

# x が 1, 2, 3 のいずれかであるかを判定する
x = 2
print(x in [1, 2, 3])
→true

#再帰関数
def f(N):
    if N ==0:
        return 0
    return N + f(N-1)

#文字列を数式として評価する
eval(str)

#文字列を逆順にする
s_reversed = ''.join(list(reversed(s)))

#リストを出力する
x = [1,2,3,4,5]
print(*x)

x = [str(i) for i in x]
print(" ".join(x))

#リストをソートする
a.sort()

#リストを反転する
a.reverse()

#リストからセットを作成する
#セットは重複、順番がない
set(a)

#リストを連結して文字列に
print("".join(ans))

#リストaからdupがどこにあるかを検索
print(a.index(dup))
#複数をリストとして返す
print([i for i, x in enumerate(a) if x==dup])

#2個以上のリストから最小公倍数を算出
def my_lcm_base(x,y):
    return (x*y)//math.gcd(x,y)
def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)
print(my_lcm(*list))