def pzn(num):
    if num>0:
        tmp=1
    elif num==0:
        tmp=0
    else:
        tmp=-1
    return tmp

while True:
    n=int(input("정수:"))
    r=pzn(n)
    if r==1:
        print("양수")
    elif r==0:
        print("0")
        break
    else:
        print("음수")
