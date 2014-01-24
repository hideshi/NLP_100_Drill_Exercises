if __name__ == '__main__':
  with open('col1.txt', 'r') as f:
    print(len(set(f.readlines())))
