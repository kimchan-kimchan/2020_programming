a=input("입력:")
b=a[-2:]

if b=="달러":
    c=float(a[:-4])
    c=c*1167
    print(c,"원")
    
elif b==" 엔":
    c=float(a[:-3])
    c=c*1.096
    print(c,"원")

elif b=="유로":
    c=float(a[:-4])
    c=c*1268
    print(c,"원")

else:
    c=float(a[:-4])
    c=c*171
    print(c,"원")




