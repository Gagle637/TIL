def concat(str1, str2):
    return f'{str1} - {str2}'
def check_long_str(string):
    if len(string) > 10:
        return True
    else:
        return False
if check_long_str(concat('Happy', 'Hacking')):
    print('LONG STRING')
else:
    print('SHORT STRING')
print(check_long_str(concat('Happy', 'Hacking')))
print(concat('Happy', 'Hacking'))