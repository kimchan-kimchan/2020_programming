mymoney=int(input("내가 가지고 있는 돈:"))

leftmoney1=mymoney
오백원=leftmoney1//500

leftmoney2=leftmoney1%500
백원=leftmoney2//100

leftmoney3=leftmoney2%100
오십원=leftmoney3//50

leftmoney4=leftmoney3%50
십원=leftmoney4//10

print('500원:',오백원,'개')
print('100원:',백원,'개')
print('50원:',오십원,'개')
print('10원:',십원,'개')
