import re
if __name__ == '__main__':
  with open('address.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip()
      re.sub('\t', ' ', line)
      print(line)
