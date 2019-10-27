while True:
    try:
        n = int(input('Nilai N ? '))    
        if n > 0:
            break
        else:
            print('your input must bigger than zero')
    except:
        print('your input must be a numeric ...')
        
i = 1
frek = 0
jlh = 0

while i <= n:
    while True:
        try:
            x = int(input(f'Nilai x [{i:2}] ? '))
            if x > 0:
                break
            else:
                print('your input must bigger than zero')
        except:
            print('your input must be a numeric ...')
    if x % 2 == 0:
        frek += 1
        jlh += x
    i += 1

print(f'Jumlah dari semua bilangan genap = {jlh:,}')
print(f'Frekuensi Kemunculan Bilangan Genap = {frek}x dari {n} percobaan')

