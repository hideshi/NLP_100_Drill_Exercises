import sys
if __name__ == '__main__':
  num = int(sys.argv[1])
  cnt = 1
  with open('address.txt', 'r') as f:
    lines = f.readlines()
    size = len(lines)
    for line in lines:
      if cnt > size - num:
        print(line.strip())
      cnt = cnt + 1
