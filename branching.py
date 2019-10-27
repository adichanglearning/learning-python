def is_numeric(str):
    try:
        int(str)
        return True
    except:
        return False
        
if __name__ == '__main__':
    while True:
        str_input = input('input a value between 0 and 100 ? ')
        if is_numeric(str_input):
            value = int(str_input)
            if (value >= 0 and value <= 100):
                break
            else:
                print('your input is not a valid value ... plz retry ...')
        else:
            print('your input is not a valid value ... plz retry ...')
            
    if value < 60:
        print(f'value = {value} => Fail.')
    else:
        print(f'value = {value} => Success.')