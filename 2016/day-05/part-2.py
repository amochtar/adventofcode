import hashlib

input = 'abbhdwsy'

index = 0
password = '________'
while '_' in password:
    md5 = hashlib.md5(input + str(index)).hexdigest()
    if md5[:5] == '00000':
        try:
            i = int(md5[5])
            if i < len(password) and password[i] == '_':
                password = password[:i] + md5[6] + password[i + 1:]
                print password
        except:
            pass
    index += 1
