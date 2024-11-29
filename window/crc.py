def xor_operation(a, b):
  return ''.join('0' if bit1 == bit2 else '1' for bit1, bit2 in zip(a, b))

def crc_generate(data, generator):
  data += '0' * (len(generator) - 1)
  gen_len = len(generator)
  data_len = len(data)
  for i in range(data_len - gen_len + 1):
    if data[i] == '1':
      data = data[:i] + xor_operation(data[i:i+gen_len], generator) + data[i+gen_len:]
  return data[-(len(generator) - 1):]

def crc_check(data, generator, remainder):
  appended_data = data + remainder
  gen_len = len(generator)
  for i in range(len(data) + len(remainder) - gen_len + 1):
    if appended_data[i] == '1':
      appended_data = appended_data[:i] + xor_operation(appended_data[i:i+gen_len], generator) + appended_data[i+gen_len:]
  return all(bit == '0' for bit in appended_data)

def main():
  data = input("Enter data binary string: ")
  generator = input("Enter CRC generator polynomial: ")
  remainder = crc_generate(data, generator)
  print(f"CRC Remainder: {remainder}")

  if crc_check(data, generator, remainder):
    print("No error detected.")
  else:
    print("Error detected.")

if __name__ == "__main__":
  main()