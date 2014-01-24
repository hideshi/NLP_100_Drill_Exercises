import re
if __name__ == '__main__':
    p = re.compile('@\w+')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.match(line)
            if m:
                print(m.group())
