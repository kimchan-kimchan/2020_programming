a=input("주민등록번호:")
s=int(a[0])*2+int(a[1])*3+int(a[2])*4+int(a[3])*5+int(a[4])*6+int(a[5])*7+int(a[7])*8+int(a[8])*9+int(a[9])*2+int(a[10])*3+int(a[11])*4+int(a[12])*5
R=11-(s&11)

if R==int(a[13]):
    print("유효한 주민등록번호입니다")
    
else:
    print("유효하지 않은 주민등록번호입니다")








