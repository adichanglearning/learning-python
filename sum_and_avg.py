while True:
    try:
        n = int(input('Banyak Bilangan ? '))
        if n > 0:
            break
    except:
        print('Numeric Plz and n > 0...')
        
i = 1
jlh = 0

while i <= n:
    while True:
        try:
            x = int(input(f'x [{i:2}] ? '))
            if x > 0:
                break
        except:
            print('value must be an int and > 0 ...')
    jlh += x
    i += 1

rata = jlh / n

print(f'Jumlah Seluruh Bilangan = {jlh:,}')
print(f'Rata - Rata             = {rata:,.2f}')