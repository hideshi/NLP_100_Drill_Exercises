if __name__ == '__main__':
  with open('address.txt', 'r') as f:
    lst = []
    for line in f.readlines():
      splitted = line.strip().split('\t')
      if len(splitted) == 1:
        splitted.append('')
      lst.append(splitted)
    lst.sort(key = lambda x : (x[1], x[0]), reverse=True)
    for item in lst:
      print('{0}\t{1}'.format(item[0], item[1]))
