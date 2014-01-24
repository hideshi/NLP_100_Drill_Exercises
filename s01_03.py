if __name__ == '__main__':
  with open('address.txt', 'r') as f:
    with open('col1.txt', 'w') as o1:
      with open('col2.txt', 'w') as o2:
        for line in f.readlines():
          col1, col2 = line.replace('\n', '').split('\t')
          o1.write(col1 + '\n')
          o2.write(col2 + '\n')
