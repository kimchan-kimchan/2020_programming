def print19(start,end):
    for i in range(start,end+1):
        print(i,end=" ")
    print("")

s=int(input("시작:"))
e=int(input("끝:"))
if s<e:
    print19(s,e)
