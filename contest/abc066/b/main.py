S = input()

for i in range(1,len(S)//2):
    S = S[:len(S)-2]
    if S[:len(S)//2] == S[len(S)//2:]:
        print(len(S))
        exit()


