v,c = input().split()
if v==c:
    print("NULL")
elif (v=='S' and c=='P') or (v=='p' and c=='R') or (v=='R' and c=='S'):
    print("Vignesh")
else:
    print("Charan")
