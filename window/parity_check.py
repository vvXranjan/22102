def add_parity_bit(binary, even_parity=True):
  count = binary.count('1')
  parity_bit = '0' if (even_parity and count % 2 == 0) or (not even_parity and count % 2 != 0) else '1'
  return binary + parity_bit

def check_parity(binary_with_parity, even_parity=True):
  count = binary_with_parity.count('1')
  return (count % 2 == 0) if even_parity else (count % 2 != 0)

def main():
  binary = input("Enter a binary string: ")
  even_parity_binary = add_parity_bit(binary, even_parity=True)
  odd_parity_binary = add_parity_bit(binary, even_parity=False)
  print(f"Binary with Even Parity: {even_parity_binary}")
  print(f"Binary with Odd Parity: {odd_parity_binary}")

# Simulate receiving the even parity string
  print("Check Even Parity: " + ("Correct" if check_parity(even_parity_binary, even_parity=True) else "Error"))
  print("Check Odd Parity: " + ("Correct" if check_parity(odd_parity_binary, even_parity=False) else "Error"))

if __name__ == "__main__":
  main()