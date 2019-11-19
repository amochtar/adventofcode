data = '01110110101001000'
disk_sizes = [272, 35651584]


def gen_data(data, disk_size):
    while len(data) < disk_size:
        b = data[::-1].replace('1', '2').replace('0', '1').replace('2', '0')
        data += '0' + b

    return data[:disk_size]


def checksum(checksum):
    while len(checksum) % 2 == 0:
        checksum = ['1' if checksum[i] == checksum[i+1] else '0' for i in range(0, len(checksum), 2)]
    return ''.join(checksum)


for disk_size in disk_sizes:
    print checksum(gen_data(data, disk_size))
