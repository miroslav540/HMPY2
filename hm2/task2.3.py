from itertools import count


polindr = str(input('Enter the number: '))
polindr1 = polindr
polindr2 = None
count = 0
while True:
    count += 1
    polindr2 = ''.join(reversed(polindr1))
    if polindr1 == polindr2:
        print("Polindrom:", polindr2)
        print(f'counts of that: {count}')
        break
    else:
        p= int(polindr1) + int(polindr2)
        polindr1 = str(p)