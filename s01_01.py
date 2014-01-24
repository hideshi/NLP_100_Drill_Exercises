if __name__ == '__main__':
  with open('address.txt', 'r') as f:
    lines = f.readlines()
    print(len(lines))
