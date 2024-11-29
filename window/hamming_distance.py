def hamming_distance(str1, str2):
  if len(str1) != len(str2):
    raise ValueError("Binary strings must be of equal length")
  return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def main():
  binary1 = input("Enter the first binary string: ")
  binary2 = input("Enter the second binary string: ")
  try:
    distance = hamming_distance(binary1, binary2)
    print(f"Hamming Distance: {distance}")
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()