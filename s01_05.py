import sys
if __name__ == '__main__':
  num = int(sys.argv[1])
  cnt = 1
  with open('address.txt', 'r') as f:
    for line in f.readlines():
      if cnt > num:
        exit(0)
      else:
        print(line.strip())
        cnt = cnt + 1
