import sys
a, a_s = sys.stdin.readline().strip().split()
b, b_s = sys.stdin.readline().strip().split()

if (a_s == 'M' and a >= '19') or (b_s == 'M' and b >= '19'):
    print(1)
else:
    print(0)
    