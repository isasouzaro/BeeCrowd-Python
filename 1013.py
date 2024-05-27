a, b, c = map(int, input().split())

maior_ab = (a + b + abs(a - b)) / 2

maior = (maior_ab + c + abs(maior_ab - c)) / 2

maior = int(maior)

print("%d eh o maior" % maior)