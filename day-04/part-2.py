import hashlib

input = 'yzbqklnj'

index = 0
while True:
    md5 = hashlib.md5(input + str(index)).hexdigest()
    if md5[:6] == '000000':
        print index, md5
        break
    index += 1
