def vsum(*num):
    s=0
    for i in num:
        s+=i
    return s

print("2+3=",vsum(2,3))
print(vsum(2,3,4))
print(vsum(2,3,4,5))
