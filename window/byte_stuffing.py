FLAG = '01111110'
ESC = '01111101'

def byte_stuffing(data):
    stuffed_data = []
    for byte in data:
        if byte == FLAG or byte == ESC:
            stuffed_data.append(ESC)
        stuffed_data.append(byte)
    return stuffed_data

def byte_unstuffing(data):
    unstuffed_data = []
    i = 0
    while i < len(data):
        if data[i] == ESC:
            i += 1
            unstuffed_data.append(data[i])
        else:
            unstuffed_data.append(data[i])
        i += 1
    return unstuffed_data

data = ['01111100', '01111110', '01111101', '01111100']
print(f"Original Data: {data}")

stuffed_data = byte_stuffing(data)
print(f"Stuffed Data: {[FLAG] + stuffed_data + [FLAG]}")

transmitted_data = [FLAG] + stuffed_data + [FLAG]

received_data = transmitted_data[1:-1]
unstuffed_data = byte_unstuffing(received_data)
print(f"Unstuffed Data: {unstuffed_data}")

assert data == unstuffed_data, "Data mismatch after unstuffing"
print("Byte stuffing and unstuffing successful!")