if __name__ == '__main__':
  with open('col2.txt', 'r') as f:
    dct = {}
    for line in f.readlines():
      col = line.strip()
      cnt = dct.get(col, 0)
      dct[col] = cnt + 1
    lst = sorted(dct.items(), key = lambda x : x[1], reverse=True)
    for key, value in lst:
      print('{0}\t{1}'.format(key, value))
