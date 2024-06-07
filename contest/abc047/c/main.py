S = input()
SL = list(S)
bcolor=""
color =""
cnt =0
for i in SL:
    bcolor = color
    color = i

    if bcolor != color:
        cnt += 1
    

print(cnt-1)    
   

"""
BBWB

"""