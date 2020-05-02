# 왼쪽 정렬
for x in range(1, 4):
    print('[{0:2d}] [{1:3d}] [{2:4d}]'.format(x, x*x, x*x*x))
print()
# 가운데 정렬
for x in range(1, 4):
    print('[{0:^2d}] [{1:^3d}] [{2:^4d}]'.format(x, x*x, x*x*x))
print()
# 오른쪽 정렬
for x in range(1, 4):
    print('[{0:<2d}] [{1:<3d}] [{2:<4d}]'.format(x, x*x, x*x*x))
print()
# 0으로 채우기
for x in range(1, 4):
    print('[{0:02d}] [{1:03d}] [{2:04d}]'.format(x, x*x, x*x*x))
print()
# 부호 출력
print('[{0:05d}] [{1:05d}] [{2:05d}]'.format(1,-2,3))    # 음수만 부호
print('[{0:+05d}] [{1:+05d}] [{2:+05d}]'.format(1,-2,3)) # 부호
print('[{0:<5d}] [{1:<5d}] [{2:<5d}]'.format(1,-2,3))     # 정렬
print('-' * 40)
