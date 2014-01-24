if __name__ == '__main__':
  with open('col1.txt', 'r') as i1:
    with open('col2.txt', 'r') as i2:
      lst1 = []
      lst2 = []
      for col1 in i1:
        lst1.append(col1)
      for col2 in i2:
        lst2.append(col2)
      cnt = 0
      for c1 in lst1:
        print(c1.strip() + '\t' + lst2[cnt].strip())
        cnt = cnt + 1
