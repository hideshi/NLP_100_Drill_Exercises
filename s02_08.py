import re
if __name__ == '__main__':
    p = re.compile('(太白|宮城野|泉|青葉|若林)区?')
    with open('tweet.txt', 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            m = p.search(line)
            if m:
                print(m.group())
