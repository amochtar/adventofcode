import hashlib

input = 'abbhdwsy'

index = 0
password = ''
while len(password) < 8:
    md5 = hashlib.md5(input + str(index)).hexdigest()
    if md5[:5] == '00000':
        password += md5[5]
        print index, md5, password
    index += 1
