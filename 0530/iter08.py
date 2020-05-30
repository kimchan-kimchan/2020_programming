odd_sum=0
even_sum=0
for i in range(101):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("홀수 합:",odd_sum)
print("짝수 합:",even_sum)
