import re
if __name__ == '__main__':
    p = re.compile('([一-龠]+)\(([A-Z]+?)\)')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.search(line)
            if m:
                print(m.group(1) + '\t' + m.group(2))
