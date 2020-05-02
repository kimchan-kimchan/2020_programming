# 두 수를 입력받아 사칙연산 결과를 출력하는 프로그램
num1=float(input("첫 번째 정수 입력:"))
num2=float(input("두 번째 정수 입력:"))

print("{:.2f} + {:.2f} = {:.2f}".format(num1,num2,(num1+num2)))
print("{:.2f} - {:.2f} = {:.2f}".format(num1,num2,(num1-num2)))
print("{:.2f} * {:.2f} = {:.2f}".format(num1,num2,(num1*num2)))
print("{:.2f} / {:.2f} = {:.2f}".format(num1,num2,(num1/num2)))
