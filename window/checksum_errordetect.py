def calculate_checksum(blocks):
  total_sum = sum(blocks)
  return (~total_sum + 1) & 0xFFFF 

def main():
  num_blocks = int(input("Enter the number of data blocks: "))
  blocks = []
  print("Enter the data blocks:")
  for _ in range(num_blocks):
    blocks.append(int(input()))
  checksum = calculate_checksum(blocks)
  print(f"Checksum: {checksum}")
  print("Send data blocks and checksum.")
  print("Enter received data blocks:")
  received_blocks = [int(input()) for _ in range(num_blocks)]
  received_checksum = calculate_checksum(received_blocks)
  if received_checksum == checksum:
    print("Data received correctly.")
  else:
    print("Error detected in data.")

if __name__ == "__main__":
  main()