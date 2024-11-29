def bit_stuffing(data):
    stuffed_data = []
    count = 0
    for bit in data:
        stuffed_data.append(bit)
        if bit == '1':
            count += 1
        else:
            count = 0
        if count == 5:
            stuffed_data.append('0')
            count = 0
    return ''.join(stuffed_data)

def bit_unstuffing(data):
    unstuffed_data = []
    count = 0
    i = 0
    while i < len(data):
        unstuffed_data.append(data[i])
        if data[i] == '1':
            count += 1
        else:
            count = 0
        if count == 5:
            i += 1
            count = 0
        i += 1
    return ''.join(unstuffed_data)

frame_start = "01111110"
frame_end = "01111110"
data = "01111110001111110"

print(f"Original Data: {data}")
stuffed_data = bit_stuffing(data)
print(f"Stuffed Data: {frame_start + stuffed_data + frame_end}")

transmitted_data = frame_start + stuffed_data + frame_end
received_data = transmitted_data[len(frame_start):-len(frame_end)]
unstuffed_data = bit_unstuffing(received_data)

print(f"Unstuffed Data: {unstuffed_data}")
assert data == unstuffed_data, "Data mismatch after unstuffing"
print("Bit stuffing and unstuffing successful!")
